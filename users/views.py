from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, ContactListForm
from django.contrib.auth.models import User

def index(request):
    # form=ContactListForm()
    # return render(request, 'users/index.html', {'form':form, 'title':'index'})
    if request.user.is_anonymous:
        return redirect('login')
    logged_in_user = request.user
    contact_list = logged_in_user.contact_list.all().order_by('dateTime')
    if request.method=="POST":
        form = ContactListForm(data=request.POST)
        if form.is_valid():
            contactlist = form.save(commit=False)
            contactlist.owner = request.user
            contactlist.save()
            return redirect('index')
    else:
        form=ContactListForm()
    return render(request, "users/index.html", {'form':form, 'title':'index', 'contact_list': contact_list})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            if User.objects.filter(username = username).first():
                messages.error(request, "This email is already taken")
                return render(request, 'users/register.html', {'form': form, 'title':'reqister here'})
            obj = form.save(commit=False)
            obj.username= username
            obj.save()
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title':'reqister here'})

def Login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            return redirect('index')
        else:
            messages.info(request, f'incorrect username or password')
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form, 'title':'log in'})
