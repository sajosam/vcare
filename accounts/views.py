from django.shortcuts import render, redirect, get_object_or_404
# from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def login(request):
    return render(request, 'accounts/login.html')


def signup(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone_number=request.POST['phone_number']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        username = email.split("@")[0]
        state=request.POST['state']
        district = request.POST['district']
        dob = request.POST['dob']
        sex=request.POST['gender']
        password=request.POST['password']
        request.session['user_district']=district
        request.session['user_state']=state
        # password validation
        if password!=confirm_password:
            messages.error(request, 'password does not match')
            return redirect('signup')
            # email exists
        elif Account.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('signup')
        else:
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password,sex=sex, state=state,dob=dob,district=district,phone_number=phone_number)
            user.save()
            messages.success(request, 'Thank you for registering with us. Please Login')
            return redirect('login')
    else:
    
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        print(email,password)

        user=auth.authenticate(email=email, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)

            messages.success(request, 'you are logged in')
            request.session['email']=email
            request.session['first_name']=user.first_name
            # store user details in session
            request.session['user_district']=user.district
            return redirect('home')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')

