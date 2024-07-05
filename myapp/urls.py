
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name='index'),
    path('product/<int:id>',views.detail,name='detail'),
    path('payement',views.payment_gateway,name='payment'),
    path('successpay',views.success,name='success'),
    path('createproduct',views.create_product,name='createproduct'),
    path('editproduct/<int:id>',views.product_edit,name='editproduct'),
    path('delete/<int:id>',views.product_delete,name='delete'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('register',views.register,name='register'),
    path('login',auth_views.LoginView.as_view(template_name='myapp/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='myapp/logout.html'),name='logout'),
    path('invalid',views.invalid,name='invalid'),


]
