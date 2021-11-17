from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import JavaShop, User, Review 
import bcrypt

# Create your views here.
def index(request): 
    return render(request, 'log-reg.html')

def createShop(request):
    # return render(request,"add-shop.html")
    errors = JavaShop.objects.shop_validator(request.POST)

    if len(errors) > 0  :
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/add')
    else :
            user = User.objects.get(id = request.session['user_id'])
            JavaShop.objects.create(
                name = request.POST['name'], 
                street_address = request.POST['street_address'], 
                city = request.POST['city'] ,
                zip_code = request.POST['zip_code'],
                hours_of_operation = request.POST['hours_of_operation'],
                phone_number = request.POST['phone_number'],
                posted_by = user
                )
                
            return redirect("/dashboard")
# def oneShop(request,id):
#     return render(request,"one-shop.html")

def oneShop(request, id):
    context = {
        'shop': JavaShop.objects.get(id = id)
    }
    return render(request, "one-shop.html", context) 

def register(request):
    if request.method == 'GET':
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request,e)
        return redirect('/')
    else:
        # new_user = User.objects.register(request.POST)
        # request.session['user_id'] = new_user.id
        # messages.success(request, "You have successfully registered!")
        # return redirect('/sucess')  
        new_user = User.objects.create(first_name = request.POST['first_name'], last_name= request.POST['last_name'], email = request.POST['email'], password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode(), user_name = request.POST['user_name'], zip_code = request.POST['zip_code'])
        request.session['user_id'] = new_user.id
        request.session['greeting'] = new_user.first_name
        return redirect('/dashboard')

def login(request):
    if request.method =='GET':
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email = request.POST['email'])
    request.session['user_id'] = user.id
    # messages.success(request, " You have successfully logged in!")
    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')
