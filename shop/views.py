from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.models import User ,auth
from.models import Product ,Contact
from math import ceil
from django.contrib import messages
def home(request):
    products= Product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,"home.html", params)

def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        phone=request.POST.get('phone', '')
        address=request.POST.get('address', '')
        if len(name)<2  or len(phone)<10 or len(address)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name,phone=phone,address=address)
            contact.save()
            messages.success(request, "Thank you for contactUs")
            return redirect('/')
    return render(request,'contact.html')



def signup(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('signup')
        else:
             user=User.objects.create_user(first_name=first_name,last_name=last_name, username=username,email=email,password=password)
             user.save()
             messages.success(request,'you are successfully signup')
             return redirect('/login/')
    return render (request,'signup.html')




def Login(request):
    if request.method=="POST":

        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=auth.authenticate(username= loginusername, password= loginpassword)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("login")

    return render(request,'Login.html')




def Logout(request):
    auth.logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

