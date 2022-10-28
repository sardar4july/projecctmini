from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        #username = request.POST.get('username')
        user_name = request.POST['username']
        first_name = request.POST['firstname']
        last_name= request.POST['lastname']
        email_id = request.POST['emailid']
        pass_word = request.POST['password']
        pass_word2 = request.POST['password2']

        if User.objects.filter(username = user_name):
            messages.error(request,"Username already exists! Try new one")
            return redirect('Home')

        if User.objects.filter(email = email_id):
            messages.error(request,'Email address already exixts! Try new one')
            return redirect('Home')

        if len(user_name)>10:
            messages.error(request,'Username should be under 10 characters')

        if pass_word != pass_word2:
            messages.error(request, 'Passwords didn\'t match')

        if not user_name.isalnum():
            messages.error(request,'Username must be alphanumeric')
            return redirect('Home')


        my_user = User.objects.create_user(user_name,email_id,pass_word)
        my_user.firstname = first_name
        my_user.lastname = last_name
        my_user.password2 = pass_word2

        my_user.save()

        messages.success(request,"Your account has been successfully created.")
        return redirect("/login")
    return render(request, 'register.html')

def loggin(request):
    if request.method == "POST":
        user_name = request.POST['username']
        pass_word = request.POST['password']

        user = authenticate(username=user_name,password = pass_word)

        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, 'index.html',{'first_name': firstname })
        else:
            messages.error(request,"Incorrect Credentials")
            return redirect('Home')
    return render(request, 'loggin.html')

def loggout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('Home')