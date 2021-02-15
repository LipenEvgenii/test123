from django.conf.urls import url
from django.urls import path
from . import views
from .views import CategoryCreate,ProductCreate,index,ShopLoginView,profile,ShopLogoutView,ShopUserRegisterView

app_name='shop'
urlpatterns = [
   path('accounts/register/', ShopUserRegisterView.as_view(),name='register'),
   path('accounts/logout',ShopLogoutView.as_view(),name="logout"),
   path('accounts/profile/',profile,name="profile"),
   path('accounts/login/',ShopLoginView.as_view(),name='login'),
   path('category/',CategoryCreate.as_view(),name='category'),
   path('product/', ProductCreate.as_view(),name='product'),
   path('api/',index),
   path('',views.product_list, name='product_list'),
   path(r'(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_by_category'),
   path(r'(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail' ),

]