from django.shortcuts import render,redirect
from django.db.models import Q
from django.http import Http404
from django.http import *
from django.contrib import messages

from django.http import HttpResponse
from django.conf import settings

from .models import Search,Register,login,applyjob
from .forms import Searchform,regform,logregform,loginform,applyform
# from .forms import *

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail
from email.mime.image import MIMEImage
from django.http import JsonResponse
import json

def aboutus(request):
    return render(request, 'aboutus.html')

def jobpages(request):
    return render(request, 'jobpages.html')

def jobs(request):
    return render(request, 'jobs.html')

def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch!=None:
            t = srch.split(",")
            l = []
            for i in t:
                print(i)
                match = Search.objects.filter(
                    Q(job__icontains=i) )
                print(match)
                if match:
                    l.append(match)
                else:
                    messages.error(request, 'Data not found Please try again .......')

            return render(request, 'search.html', {'sr':l})
        else:
            messages.sucess("enter data")
    else:
        return render(request, 'search.html')

def register(request):
    if request.method == "POST":
        fform=regform(request.POST,request.FILES)
        if fform.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            location=request.POST.get('location')
            job=request.POST.get('job')
            cv=fform.cleaned_data.get('cv')
            
          
            data=Register(
                name=name,
                email=email,
                phone=phone,
                location=location,
                job=job,
                cv=cv,
                
                )
            data.save()
            fform=regform()
            fdata = Register.objects.all()
            return render(request,'register.html',{'fform': fform,'fdata': fdata})
        else:
            return HttpResponse('Invalid User Data')
    else:
        fform = regform()
        fdata = Register.objects.all()
    return render(request, 'register.html',{'fform': fform,'fdata': fdata})


def loginview(request):
    if request.method == "POST":
        fform=logregform(request.POST)
        if fform.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            
          
            data=login(
                username=username,
                password=password,
                email=email,
               
                )
            data.save()
            fform=logregform()
            fdata = login.objects.all()
            return render(request,'login.html',{'fform': fform,'fdata': fdata})
        else:
            return HttpResponse('Invalid User Data')
    else:
        fform = logregform()
        fdata = login.objects.all()
    return render(request, 'login.html',{'fform': fform,'fdata': fdata})


def login_in(request):
    if request.method=="POST":
        lform=loginform(request.POST)
        if lform.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')

            uname=login.objects.filter(username=username)
            pwd=login.objects.filter(password=password)

            data=login(
                username=username,
                password=password
                )
            g=data.username
            print(g)


            if uname and pwd:
                return render(request, 'jobpages.html',{'g':g})
            else:
                return HttpResponse("login fail")
        else:
            return HttpResponse("Invalid")
    else:
        lform=loginform()
        return render(request, 'login.html',{'lform': lform})

def apply_job(request):
    if request.method == "POST":
        fform=applyform(request.POST,request.FILES)
        if fform.is_valid():
            fullname=request.POST.get('fullname')
            email=request.POST.get('email')
            message=request.POST.get('message')
            cv=fform.cleaned_data.get('cv')
            
          
            data=applyjob(
                fullname=fullname,
                email=email,
                message=message,
                cv=cv,
                
                )
            data.save()
            fform=applyform()
            fdata = applyjob.objects.all()
            return render(request,'jobreg.html',{'fform': fform,'fdata': fdata})
        else:
            return HttpResponse('Invalid User Data')
    else:
        fform = applyform()
        fdata = applyjob.objects.all()
    return render(request, 'jobreg.html',{'fform': fform,'fdata': fdata})
