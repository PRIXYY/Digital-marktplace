from django.shortcuts import render,redirect
from .models import Product,OrderDetail
from .forms import ProductForm,UserRegisterationForm
from django.db.models import Sum
import datetime
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return render(request, 'myapp/logout.html')
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'myapp/index.html',{'products':products})

def detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,'myapp/detail.html',{'product':product})

def payment_gateway(request,id):
    product = Product.objects.get(id=id)
    order = OrderDetail()
    order.customer_name= request.user
    order.product = product.name
    order.amount = product.price
    product.total_sales_amount = product.total_sales_amount + int(product.price)
    product.total_sales = product.total_sales + 1
    product.save()
    order.save()
    return render(request,'myapp/payement.html')
    

def success(request):
    return render(request,'myapp/success_pay.html')

    



def create_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST,request.FILES)
        if product_form.is_valid():
            new_product = product_form.save(commit=False)
            new_product.seller = request.user
            new_product.save()
            return redirect('index')

    product_form = ProductForm()
    return render(request,'myapp/create_product.html',{'product_form':product_form})

def product_edit(request,id):
    product = Product.objects.get(id=id)
    if product.seller != request.user:
        return redirect('invalid')
    
    product_form = ProductForm(request.POST or None,request.FILES or None,instance=product)
    if request.method == 'POST':
        if product_form.is_valid():
            product_form.save()
            return redirect('index')
    return render(request,'myapp/product_edit.html',{'product_form':product_form,'product':product})

def product_delete(request,id):
    product = Product.objects.get(id=id)
    if product.seller != request.user:
        return redirect('invalid')
    
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    return render(request,'myapp/delete.html',{'product':product})

def dashboard(request):
    products = Product.objects.filter(seller=request.user )
    return render(request,'myapp/dashboard.html',{'products':products})

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterationForm(request.POST)
        new_user = user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        return redirect('index')
    user_form = UserRegisterationForm()
    return render(request,'myapp/register.html',{'user_form':user_form})

def invalid(request):
    return render(request,'myapp/invalid.html')

def my_purchases(request):
    orders = OrderDetail.objects.filter(customer_name=request.user)
    return render(request,'myapp/purchases.html',{'orders':orders})

def sales(request):
    orders = OrderDetail.objects.filter(customer_name=request.user)
    total_sales = orders.aggregate(Sum('amount'))
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = OrderDetail.objects.filter(customer_name=request.user,created_on__gt=last_year)
    yearly_sales = data.aggregate(Sum('amount'))
    
    #30 day sales sum
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = OrderDetail.objects.filter(customer_name=request.user,created_on__gt=last_month)
    monthly_sales = data.aggregate(Sum('amount'))
    
    #7 day sales sum
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = OrderDetail.objects.filter(customer_name=request.user,created_on__gt=last_week)
    weekly_sales = data.aggregate(Sum('amount'))
    
    #Everday sum for the past 30 days
    daily_sales_sums = OrderDetail.objects.filter(customer_name=request.user).values('created_on__date').order_by('created_on__date').annotate(sum=Sum('amount'))
    
    
    
    product_sales_sums = OrderDetail.objects.filter(customer_name=request.user).values('product').order_by('product').annotate(sum=Sum('amount'))
    print(product_sales_sums)

    return render(request, 'myapp/sales.html',{'total_sales':total_sales,'yearly_sales':yearly_sales,'monthly_sales':monthly_sales,'weekly_sales':weekly_sales,'daily_sales_sums':daily_sales_sums,'product_sales_sums':product_sales_sums})