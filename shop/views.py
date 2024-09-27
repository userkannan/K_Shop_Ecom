from django.shortcuts import render,redirect
from shop.forms import CustomUserForm
from  . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json



# Create your views here.
def home(request):
    pro=Product.objects.filter(trending=1)
    return render(request,"htmlfile/index.html",{"pro":pro})

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect("/login")
    return render(request,"htmlfile/login.html")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Successfully")
    return redirect("/")

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Reegistration Success You Can Login Now..!")
            return redirect('/login')
    return render(request,"htmlfile/register.html",{"form":form})

def catagory(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"htmlfile/catagory.html",{"catagory":catagory})

def catagoryview(request,name):
    if(Catagory.objects.filter(name=name,status=0)):
        product=Product.objects.filter(catagory__name=name)
        return render(request,"htmlfile/products/index.html",{"product":product,"catagory_name":name})
    else:
        messages.warning(request,"No Such Catagory Found ")
        return redirect('catagory')
    
def cart(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,"htmlfile/cart.html",{"cart":cart})
    else:
        return redirect("/") 
    
def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            product=Product.objects.filter(name=pname,status=0).first()
            return render(request,"htmlfile/products/product_details.html",{"product":product})
        else:
            messages.error(request,"No Such Product Found")
            return redirect('catagory')           
    else:
        messages.error(request,"No such Catagory Found")
        return redirect('catagory')
    
def add_cart(request):
    if request.headers.get('X-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            # print(request.user.id)
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Cart'},status=200)
                else:
                    if product_status.quantity>=product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product Add to Cart'},status=200)
                    else:
                        return JsonResponse({'status':'Product Stock Not Available'},status=200)
        else:
            return JsonResponse({'status':'Login to Add Cart'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)
    
def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")

def heart(request):
    if request.headers.get('X-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id=data['pid']
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Heart.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Favouite'},status=200)
                else:
                    Heart.objects.create(user=request.user,product_id=product_id)
                    return JsonResponse({'status':'Product Added to Favourite'},status=200)
        else:
            return JsonResponse({'status':'Login to Add Favourite'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)
    
def heart_page(request):
    if request.user.is_authenticated:
        heart=Heart.objects.filter(user=request.user)
        return render(request,"htmlfile/heart.html",{"heart":heart})
    else:
        return redirect("/")
    
def remove_heart(request,hid):
    cartitem=Heart.objects.get(id=hid)
    cartitem.delete()
    return redirect("/heart_page")
    
    
    
    
