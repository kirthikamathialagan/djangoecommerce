from django.urls import path
from . import views
app_name="cart"
urlpatterns = [
    path('',views.cart_detail,name="cart_detail"),
    path('add/<int:product_id>',views.add_cart,name='add_cart'),
    path('minus/<int:product_id>',views.cart_minus,name='cart_minus'),
    path('delete/<int:product_id>',views.delete,name='delete'),

]