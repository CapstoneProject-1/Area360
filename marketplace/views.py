from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

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
                messages.error(request,'Password is too short')
            
            elif len(phoneno) < 10:
                messages.error(request,'Contact no is wrong')

            else:
                # response = 'otp/'+phoneno+'/'

                return redirect(reverse('realestate:otp',kwargs={'phoneno':phoneno}))

        except Exception as e:
            print(e)
            return redirect('auth/register/')

    return render(request,'register.html')
        

def otp(request, phoneno):
    context = {'phoneno': phoneno}
    return render(request,'otp.html', context)

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