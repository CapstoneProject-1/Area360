from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('auth/register/',views.register, name="register"),
    path('auth/login/',views.login, name="login"),
    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name="about"),
    path('terms&conditions/',views.tc, name="tc"),
    path('privacypolicy/',views.privacypolicy, name="privacypolicy"),
    path('marketplace/',views.marketplace, name="marketplace"),
    path('property/',views.property, name="property"),
]
