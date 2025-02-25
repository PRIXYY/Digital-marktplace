from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name='index'),
    path('product/<int:id>',views.detail,name='detail'),
    path('payement/<int:id>',views.payment_gateway,name='payment'),
    path('successpay',views.success,name='success'),
    path('createproduct',views.create_product,name='createproduct'),
    path('editproduct/<int:id>',views.product_edit,name='editproduct'),
    path('delete/<int:id>',views.product_delete,name='delete'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('register',views.register,name='register'),
    path('login',auth_views.LoginView.as_view(template_name='myapp/login.html'),name='login'),
    path('logout',views.logout_view,name='logout'),
    path('invalid',views.invalid,name='invalid'),
    path('purchases',views.my_purchases,name='purchases'),
    path('sales',views.sales,name='sales'),

]
