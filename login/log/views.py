from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def demo(request):
    if request.method == 'POST':
        name = request.POST['txt']
        Email = request.POST['email']
        password = request.POST['pswd']

        user = User.objects.create_user(username=name, email=Email, password=password)
        user.save()
        messages.info(request, 'registered successfully')
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        Email = request.POST['email']
        password = request.POST['pswd']
        user = auth.authenticate(email=Email, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            messages.info(request, 'invalid password')
    return render(request,'index.html')