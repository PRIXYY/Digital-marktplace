
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('product/<int:id>',views.detail,name='detail'),
    path('payement',views.payment_gateway,name='payment'),
    path('successpay',views.success,name='success'),
    path('createproduct',views.create_product,name='createproduct'),

]
