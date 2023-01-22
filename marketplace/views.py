from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from marketplace.otp import *
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random
import http.client


# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        emailid = request.POST.get('emailid')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        usertype = request.POST.get('usertype')
        list1 = [fname,lname,emailid,password,phoneno,usertype]
        print(list1)

        try:
            if len(password) < 6:
                messages.error(request,'Password is too short.')
            
            if len(phoneno) < 10:
                messages.error(request,'Contact no is wrong.')

            else:
                if User.objects.filter(email = emailid).first():
                    messages.error(request,'Email id is taken.')
                    return redirect('realestate:auth/register/')
                if Profile.objects.filter(phoneno = phoneno).first():
                    messages.error(request,'Contact no is taken.')
                    return redirect('realestate:auth/register/')
                user_obj = User(first_name=fname, last_name=lname, username=fname+lname ,email=emailid)
                user_obj.set_password(password)
                user_obj.save()
                otp = str(random.randrange(1000,9999))
                profile_obj = Profile.objects.create(user=user_obj, phoneno=phoneno, usertype=usertype, otp=otp)
                profile_obj.save()
                # send_otp_code(phoneno, otp)
                request.session['phoneno'] = phoneno
                return redirect(reverse('realestate:otp',kwargs={'phoneno':phoneno}))
        except Exception as e:
            print(e)
    return render(request,'register.html') 

def otp(request, phoneno):
    if request.method == 'POST':
        otp1 = request.POST.get('otp1')
        otp2 = request.POST.get('otp2')
        otp3 = request.POST.get('otp3')
        otp4 = request.POST.get('otp4')
        otp = str(otp1+otp2+otp3+otp4)
        print(otp)
        # verifyotp(phoneno,otp)
        data = Profile.objects.get(phoneno=phoneno)
        if otp == data.otp:
            data.is_verified = True
            data.save()
            messages.success(request,'Contact no succssfully verified.')
            return redirect('/otp-success')
        else:
            messages.error(request,'Please enter valid OTP.')
            

    context = {'phoneno': phoneno}
    return render(request,'otp.html', context) 

def otpsuccess(request):
    return render(request,'otpsuccess.html')

def login(request):
    return render(request,'login.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def tc(request):
    return render(request,'t&c.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')

def marketplace(request):
    return render(request,'marketplace.html')

def property(request):
    return render(request,'singleproperty.html')