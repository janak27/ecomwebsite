from django.core import paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import order, products
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
import random
from django.views import View
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required

# Create your views here.
# from django.forms.models import model_to_dict
from django.contrib.auth import logout
import json
from django.http import HttpResponseRedirect
from django.urls import reverse

class Login(View):
    template_name='shop/login.html'
    def get(self, request):
    
        return render(request,self.template_name )
    def post(self, request, *args, **kwargs):
        print(request.POST)

        print(request.POST)
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
              
                messages.add_message(request, messages.INFO, 'Login successful')
                print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
                return render(request,self.template_name)        
            else:
                
                print("KKK;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
                messages.add_message(request, messages.INFO, 'Login fail')
                return render(request,self.template_name,)
            
        except IntegrityError as e:
            print("dddddddddddddddddddddddddddddddddddddddddddddddddd")
            messages.warning(request, 'User with sameusername exist')
            return render(request,self.template_name, {'falure': "userexist"})  
        

        return render(request,self.template_name,)
class Register(View):
    template_name='shop/register.html'
    def get(self, request):
        # print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
        
        return render(request,self.template_name )
    def post(self, request, *args, **kwargs):
        print(request.POST)
        try:
            user=User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password1"])
            print(user)
            
            messages.add_message(request, messages.INFO, 'UserCreated sucessfully')
        except IntegrityError as e:
            # print("dddddddddddddddddddddddddddddddddddddddddddddddddd")
            messages.warning(request, 'User with sameusername exist')
            return render(request,self.template_name, {'falure': "userexist"})        

        return render(request,self.template_name, {'sucess': True})

def logout_view(req):
    logout(req)
    return HttpResponseRedirect('/')

def index(request):

    print('helooooooooooooooooooooooooooooo')    
    product_objects = products.objects.all()
    template_name = 'shop/index.html'

    try:
        product_objects=product_objects[:3]
    except Exception as e:
        print('errrorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
    print(product_objects)


    return render(request,template_name,{'product_objects': product_objects})


def detail(request,obj_id):
    product_objects = products.objects.get(id=obj_id)
    product_objectss=products.objects.all()
    product_objectss=random.choices(product_objectss, k=4)
    

        
    

    return render(request,'shop/detail.html',{'product_objects':product_objects,"product_objectss":product_objectss})



def checkout(request):

    if request.user.is_authenticated == False:
        messages.add_message(request, messages.INFO, 'Login before acessing cart')
        return HttpResponseRedirect(reverse("login_custom"))



    if request.method == 'POST':

        items =request.POST.get('items',"") #allow the null value thats why put the empty string ""
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")

        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total','')
        order_list = order( items = items,name = name, email = email, address = address,user=request.user, city = city, state = state, zipcode = zipcode,total = total)
        order_list.save()
        messages.add_message(request, messages.INFO, 'checkout sucessfull')

    return render(request,'shop/checkout.html')

def cart(req):
    product_objects = products.objects.all()
        
    a=serialized_obj = serialize('json',product_objects )
    print(a)

    return render(req,'shop/cart.html',{'product_objects': product_objects,"a":a}   )
 


def product_list(request):
    product_objects = products.objects.all()

    return render(request,'shop/product.html',{'product_objects': product_objects})