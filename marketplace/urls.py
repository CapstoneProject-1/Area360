from django.urls import path
from . import views

app_name = 'realestate'

urlpatterns = [
    path('',views.index, name="index"),
    path('otp-success/',views.otpsuccess, name="otpsuccess"),
    path('auth/register/',views.register, name="register"),
    path('auth/login/',views.login, name="login"),
    path('auth/register/otp/<phoneno>/',views.otp, name="otp"),
    path('auth/register/resendotp/',views.resendotp, name="resendotp"),

    path('marketplace/',views.marketplace, name="marketplace"),
    path('property/',views.property, name="property"),

    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name="about"),
    path('terms&conditions/',views.tc, name="tc"),
    path('privacypolicy/',views.privacypolicy, name="privacypolicy"),
]
