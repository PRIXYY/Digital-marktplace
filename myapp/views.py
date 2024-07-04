from django.shortcuts import render
from .models import Product,OrderDetail
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'myapp/index.html',{'products':products})

def detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,'myapp/detail.html',{'product':product})

def payment_gateway(request):
    return render(request,'myapp/payement.html')



def success(request):
    return render(request,'myapp/success_pay.html')