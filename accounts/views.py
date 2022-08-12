from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import request
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.
def  signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username Already Exist")
                redirect('login_page')
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email Already Exist")
                redirect('login_page')
            else:
                messages.success(request,f"{username} Successfully Created")
                user=User.objects.create_user(first_name=username,username=username,email=email,password=password)
                user.save()
                redirect('login_page')
    
    return render(request,'signup.html')

    
def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/user/home')
        else:
            messages.error(request,"invalid Username or Password")
            return redirect('login_page')
    else:
        return render(request,'login.html')




