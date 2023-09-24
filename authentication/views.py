from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
from django.contrib.auth import authenticate,login

from django.contrib.auth.models import Group, Permission

# Create your views here.

def register(request):
    if request.method=="POST":
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        register=Register()
        register.first_name=f_name
        register.last_name=l_name
        register.username=username
        register.email=email
        register.password=password
        register.save()

        return redirect('register')
    return render(request,'authentication/register.html')

def check_username(request):
    username = request.GET.get('username')
    is_unique = not Register.objects.filter(username=username).exists()
    return JsonResponse({'unique': is_unique})


def login(request):
    if request.method=="POST":
        login_email=request.POST['login_email']
        login_password=request.POST['login_password']

        user=authenticate(email=login_email,password=login_password)

        if user is not None:
            login(request,user)
            return redirect('login')
        else:
            return render(request,'authentication/login.html',{'error_message':'Invalid username or password'})


    return render(request,'authentication/login.html')



def sidebar_menu(request):
    return render(request,'sidebar_base.html')




def add_group(request):
    all_permissions=Permission.objects.all()
    if request.method=="POST":
        g_number=request.POST['g_number']
        g_name=request.POST['g_name'].lower()
        g_permission=request.POST.getlist('g_permission')
        user_permission=[]
        for i in g_permission:
            user_permission.append(int(i))
        print(user_permission)
        group,created=Group.objects.get_or_create(id=g_number,name=g_name)
        permissions=Permission.objects.filter(codename__in=user_permission)
        group.permissions.set(user_permission)
        group.save()
        return redirect('add_group')
    
    return render(request,'authentication/add_group.html',{'permissions': all_permissions})
    

def home(request):
    return render(request,'main_content.html')


