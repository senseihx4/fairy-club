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
    path('logout/', auth_views.LogoutView.as_view(next_page='login_user'), name='logout'),
]