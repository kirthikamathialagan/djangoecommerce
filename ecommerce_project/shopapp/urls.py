from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name='shopapp'

urlpatterns = [
    path('',views.AllProductCategory,name='AllProductCategory'),
    path('<slug:c_slug>/',views.AllProductCategory, name="products_by_category"),
    path('<slug:c_slug>/<slug:p_slug>/',views.Productdetail, name="Product_cat_detail")
]