from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
import requests
from dashboard.models import *
from marketplace.otp import *
from .models import *
from django.contrib.auth import authenticate, login, logout
import random
from django.contrib.auth.models import Group
from django.core.mail import send_mail


# Create your views here.
def index(request):
    properties = Property_image.objects.all()[0:20]
    context = {"properties": properties}
    return render(request, 'index.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        emailid = request.POST.get('emailid')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        usertype = request.POST.get('usertype')
        # list1 = [username,emailid,password,phoneno,usertype]
        # print(list1)

        try:
            if len(password) < 6:
                messages.error(request, 'Password is too short.')

            if len(phoneno) < 10:
                messages.error(request, 'Contact no is wrong.')

            else:
                if User.objects.filter(username=username).first():
                    messages.error(request, 'Username is taken.')
                    return redirect('realestate:auth/register/')
                if User.objects.filter(email=emailid).first():
                    messages.error(request, 'Email id is taken.')
                    return redirect('realestate:auth/register/')
                if Profile.objects.filter(phoneno=phoneno).first():
                    messages.error(request, 'Contact no is taken.')
                    return redirect('realestate:auth/register/')

                user_obj = User(username=username, email=emailid)
                user_obj.set_password(password)
                user_obj.save()
                otp = str(random.randrange(1000, 9999))
                profile_obj = Profile.objects.create(
                    user=user_obj, phoneno=phoneno, usertype=usertype, otp=otp)
                profile_obj.save()
                if profile_obj.is_verified:
                    messages.error(request, 'Contact no already verified.')
                    return redirect('realestate:auth/register/')
                else:
                    send_otp_code(phoneno, otp)
                    request.session['phoneno'] = phoneno
                    group = Group.objects.get(name=usertype)
                    user_obj.groups.add(group)
                return redirect(reverse('realestate:otp', kwargs={'phoneno': phoneno}))
        except Exception as e:
            print(e)
    return render(request, 'register.html')


def otp(request, phoneno):
    if request.method == 'POST':
        otp1 = request.POST.get('otp1')
        otp2 = request.POST.get('otp2')
        otp3 = request.POST.get('otp3')
        otp4 = request.POST.get('otp4')
        otp = str(otp1+otp2+otp3+otp4)
        print(otp)
        data = Profile.objects.get(phoneno=phoneno)
        if otp == data.otp:
            data.is_verified = True
            data.save()
            messages.success(request, 'Contact no succssfully verified.')
            return redirect('/otp-success')
        else:
            messages.error(request, 'Please enter valid OTP.')

    context = {'phoneno': phoneno}
    return render(request, 'otp.html', context)


def resendotp(request):
    phoneno = request.session['phoneno']
    print(phoneno)
    data = Profile.objects.get(phoneno=phoneno)
    otp = str(random.randrange(1000, 9999))
    data.otp = otp
    data.save()
    # print(otp)
    send_otp_code(phoneno, otp)
    return redirect(reverse('realestate:otp', kwargs={'phoneno': phoneno}))


def otpsuccess(request):
    return render(request, 'otpsuccess.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()

        if user_obj is None:
            messages.error(request, 'User not found')
            return redirect('/auth/login')

        profile_obj = Profile.objects.filter(user=user_obj).first()

        if not profile_obj.is_verified:
            messages.error(
                request, 'User is not verified pls verify your contact no')
            return redirect('/auth/login')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('/')
        else:
            messages.error(request, 'Wrong password or email')
            return redirect('/auth/login')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'logged out')
    return redirect('/')


def contact(request):
    if request.method == 'POST':
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        msg = request.POST.get('message')

        try:
            message = fn + ln + email + msg
            send_mail(subject, message, email, [settings.EMAIL_HOST_USER])
            messages.success(request, 'successfully send')
            return redirect('/')
        except Exception as e:
            print(e)
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def tc(request):
    return render(request, 't&c.html')


def privacypolicy(request):
    return render(request, 'privacypolicy.html')


def marketplace(request):
    states_url = "https://api.countrystatecity.in/v1/countries/IN/states"
    cities_url = "https://api.countrystatecity.in/v1/countries/IN/cities"
    headers = {
        'X-CSCAPI-KEY': 'blhwU1g0VUZ4Wm1lck8zeTg5WjZIN1dvZ0JHR09NUmJrcjlTYzVRZw=='
    }
    states = requests.request("GET", states_url, headers=headers).json()
    cities = requests.request("GET", cities_url, headers=headers).json()
    property_type = Property_type.objects.all()

    # searchbar
    propertytype = ""
    purpose = ""
    state = ""
    city = ""
    properties = None
    if request.method == 'POST':
        propertytype = request.POST.get('propertytype')
        purpose = request.POST.get('purpose')
        state = request.POST.get('state')
        city = request.POST.get('city')

    try:
        property_obj = Property.objects.get(
        property_type=propertytype, property_purpose=purpose, property_state=state, property_city=city)
        properties = Property_image.objects.filter(property=property_obj)
    except Property.DoesNotExist:
        properties = Property_image.objects.all()
    
    context = {"properties": properties, "property_type": property_type, "cities": cities, "states": states}
    return render(request, 'marketplace.html', context)


def property(request, slug):
    property1 = Property_image.objects.filter(slug=slug)
    profile = Profile.objects.filter()
    context = {"propertydetails": property1, "profile": profile}

    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     contactno = request.POST.get('contactno')
    #     property_obj = Property(property)
    #     obj = Buyer(property=property_obj, name=name,contactno=contactno)
    #     print(obj)
    #     obj.save()
    #     if request.user == "Buyer":
    #         messages.success(request, 'Your request send to the seller.')
    return render(request, 'singleproperty.html', context)
