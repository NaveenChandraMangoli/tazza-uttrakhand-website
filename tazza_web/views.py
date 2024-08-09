from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from data.models import Product,Contact
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest


def index(request):
    Addproducts = Product.objects.all()
    if request.method=="GET":
        st = request.GET.get("search_item")
        if st != None:
             #search the items by this query
             #< __icontains > -> you can search item by only single letters
            Addproducts = Product.objects.filter(product_name__icontains = st) 
    data ={
        'Addproducts':Addproducts,
        }
    return render(request, "index.html",data)

def about(request):
    return render(request, "about.html")

@auth
def contact(request):

    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        msg = request.POST.get('msg', '')
        contact = Contact(name=name,email=email,phone=phone,address=address,msg=msg)
        contact.save()
        
    return render(request,"contact.html")

def gallery(request):
    return render(request, "gallery.html")

@auth
def product(request,myid):
    product = Product.objects.filter(id=myid)
    return render(request,"product.html",{'product':product[0]})

def error(request):
    return render(request, "404.html")

def all_product(request):
    Addproducts = Product.objects.all()
    if request.method=="GET":
        st = request.GET.get("search_item")
        if st != None:
             #search the items by this query
             #< __icontains > -> you can search item by only single letters
            Addproducts = Product.objects.filter(product_name__icontains = st) 
    data ={
        'Addproducts':Addproducts,
        }
    return render(request, "all_product.html",data)

# registeration page
@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    else:
        initial_data = {'username':'', 'password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html',{'form':form})

#login page
@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('index')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form}) 

# logout page
def logout_view(request):
    logout(request)
    return redirect('login')