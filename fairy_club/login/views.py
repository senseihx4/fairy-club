from django.http import HttpResponse
from django.shortcuts import render
from .forms import MembershipTypeForm
from django.contrib.auth import login
from .forms import Fairytype, UserForm, ProfileForm
from .models import User, globalmail, MailReply, podcast as PodcastModel, uploadedpodcast
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
import random
from django.shortcuts import  get_object_or_404

def home_page(request):
    return render(request, 'home.html')

def signup(request):
    form = UserForm()
    return render(request, 'signup.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
             messages.error(request, 'Email already exists.')
             return render(request, 'signup.html', {'form': form})
        
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.verification_token = str(random.randint(100000, 999999))
            user.is_verified = False
            user.save() 
            request.session['verify_email'] = user.email

            send_mail(
                subject='Your Fairy Club Verification Code',
                message=f'Your OTP is: {user.verification_token}\n\nThis code is valid for one use only.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return redirect('verify_otp') 
                
    else:
        form = UserForm()
        
               
    return render(request, 'signup.html', {'form': form}) 



def verify_otp(request):
    email = request.session.get('verify_email')

    if not email:
        return HttpResponse("Session expired. Please signup again.")

    user = User.objects.filter(email=email).first()

    if not user:
        return HttpResponse("User not found.")

    if request.method == "POST":
        entered_otp = request.POST.get('otp')
    
        if entered_otp == user.verification_token:
            user.is_verified= True
            user.verification_token = None
            user.save()
            login(request, user)

            return redirect('create_profile')

        else:
            return HttpResponse("Invalid OTP")

    return render(request, "otp.html")

def create_profile(request):
    form = ProfileForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('select_court')
    return render(request, 'create_profile.html', {'form': form})

def select_court(request):
    form = Fairytype(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('plan')
    return render(request, 'select_court.html', {'form': form})
def plan(request):
    form = MembershipTypeForm(request.POST or None, instance=request.user)
    if form.is_valid():
        selected_type = form.cleaned_data['membership_type']
        if selected_type == 1:
            return redirect('fairy_time')
        elif selected_type == 2:
            return redirect('fairy_circle')
        elif selected_type == 3:
            return redirect('fairy_world')

    return render(request, 'plan.html', {'form': form})

def fairy_time(request):
    return render(request, 'fairy_time.html')

def fairy_circle(request):
    return render(request, 'fairy_circle.html')

def fairy_world(request):
    return render(request, 'fairy_world.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()

        if user and user.check_password(password):
            if user.is_verified:
                login(request, user)
                return redirect('main_page')
            else:
                messages.error(request, 'Account not verified. Please check your email for the OTP.')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login_user.html')

def main_page(request):
    fairy_images = ['r1.png', 'r2.png', 'r3.png', 'r4.png', 'r5.png', 'r6.png']
    mails = globalmail.objects.order_by('-created_at')[:6]
    mail_list = [(mail, fairy_images[i % len(fairy_images)]) for i, mail in enumerate(mails)]
    return render(request, 'main_page.html', {'mail_list': mail_list})

def reply_mail(request, mail_id):
    mail = get_object_or_404(globalmail, id=mail_id)
    if request.method == 'POST':
        reply_content = request.POST.get('reply_content')
        send_mail(
            subject=f"Reply to: {mail.mailtitel}",
            message=reply_content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email],
            fail_silently=False,
        )
        messages.success(request, 'Reply sent successfully!')
        return redirect('main_page')
    return render(request, 'reply_mail.html', {'mail': mail})


def edit_profile(request):
    profile = get_object_or_404(User, id=request.user.id)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('main_page')

    return render(request, 'edit_profile.html', {'form': form})


def manage_subscription(request):
    return render(request, 'manage_subscription.html')

MEMBERSHIP_UPLOAD_LIMITS = {
    1: 3,   # fairy time
    2: 6,   # fairy circle
    3: 20,  # fairy world
}

def podcast(request):
    upload_count = 0
    upload_limit = 0
    can_upload = False
    user_podcast_ids = set()
    if request.user.is_authenticated:
        upload_limit = MEMBERSHIP_UPLOAD_LIMITS.get(request.user.membership_type, 0)
        upload_count = uploadedpodcast.objects.filter(user=request.user).count()
        can_upload = upload_count < upload_limit
        user_podcast_ids = set(uploadedpodcast.objects.filter(user=request.user).values_list('podcast_id', flat=True))
    podcasts = PodcastModel.objects.filter(id__in=user_podcast_ids).order_by('-created_at')
    return render(request, 'podcast.html', {
        'podcasts': podcasts,
        'upload_count': upload_count,
        'upload_limit': upload_limit,
        'can_upload': can_upload,
        'user_podcast_ids': user_podcast_ids,
    })

def delete_podcast(request, podcast_id):
    if request.method == 'POST' and request.user.is_authenticated:
        uploaded = uploadedpodcast.objects.filter(podcast_id=podcast_id, user=request.user).first()
        if uploaded:
            podcast_obj = uploaded.podcast
            uploaded.delete()
            podcast_obj.delete()
    return redirect('podcast')

def upload_podcast(request):
    if request.method == 'POST':
        user = request.user
        upload_limit = MEMBERSHIP_UPLOAD_LIMITS.get(user.membership_type, 0)
        upload_count = uploadedpodcast.objects.filter(user=user).count()
        if upload_count >= upload_limit:
            messages.error(request, 'You have reached your upload limit. Please upgrade your membership to upload more videos.')
            return redirect('podcast')
        title = request.POST.get('podcasttitel')
        video = request.FILES.get('video')
        thumbnail = request.FILES.get('thumbnail')
        p = PodcastModel(podcasttitel=title, video=video, thumbnail=thumbnail)
        p.save()
        uploadedpodcast.objects.create(podcast=p, user=user)
        return redirect('podcast')
    return redirect('podcast')
