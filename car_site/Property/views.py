from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from .models import Member
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    teams = Member.objects.all()
    
    data = {
        'teams':teams,
        
    }
    
    return render(request, 'index.html',data )

def about(request):
    teams = Member.objects.all()
    data = {
        'teams':teams
    }
    return render(request, 'pages/about.html',data)

def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')

def login(request):
    if request.method == 'POST':
        email= request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email= email,password=password)
        if user is not None:
            form = login(request,user)
            messages.success(request,"Successfully Login")
            return redirect('/')
        else:
            messages.error(request,"Something went wrong")
            return redirect('/login')
    form = AuthenticationForm()
    return render(request, 'login.html')

def signup(request):
    if request.method== 'POST':
        name = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']
        if pass1 != pass2:
            messages.error(request,"Passwords are not matching pls check once again")
            return render(request, 'signup.html')
        else:
            user = User.objects.create(username= name, email= email, password= pass1)
            user.save()
            messages.error(request,"Account created successfully")
            return redirect('/signup')
    return render(request, 'signup.html')