from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('signup/', views.signup, name='signup'),
    path('register/', views.register_user, name='register_user'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path("create_profile/", views.create_profile, name="create_profile"),
    path("select_court/", views.select_court, name="select_court"),
    path("fairy_time/", views.fairy_time, name="fairy_time"),
    path("fairy_circle/", views.fairy_circle, name="fairy_circle"),
    path("fairy_world/", views.fairy_world, name="fairy_world"),
    path("plan/", views.plan, name="plan"),
    path('login/', views.login_user, name='login_user'),
    path('main_page/', views.main_page, name='main_page'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('manage_subscription/', views.manage_subscription, name='manage_subscription'),
    path('reply_mail/<int:mail_id>/', views.reply_mail, name='reply_mail'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login_user'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html') , name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html') , name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_your_password.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),

]