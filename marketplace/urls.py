from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'realestate'

urlpatterns = [
    path('',views.index, name="index"),
    path('otp-success/',views.otpsuccess, name="otpsuccess"),
    path('auth/register/',views.register, name="register"),
    path('auth/login/',views.signin, name="login"),
    path('auth/register/otp/<phoneno>/',views.otp, name="otp"),
    path('auth/register/resendotp/',views.resendotp, name="resendotp"),
    path('auth/logout/',views.user_logout, name = 'logout'),
    
    path('marketplace/',views.marketplace, name="marketplace"),
    path('property/<slug>',views.property, name="property"),
    
    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name="about"),
    path('terms&conditions/',views.tc, name="tc"),
    path('privacypolicy/',views.privacypolicy, name="privacypolicy"),
]