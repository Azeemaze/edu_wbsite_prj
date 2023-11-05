from django.urls import path
from .import views
from .views import PasswordChangeView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),
    path('Registration/',views.RegistrationF,name='RegistrationF'),
    path('signup',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('password/', PasswordChangeView.as_view(),name='password'),
    path('password_success/', views.password_success, name='password_success'),
    path('courses/', views.courses, name='courses'),

    #Password Reset urls
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]