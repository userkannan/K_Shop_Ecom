from django.urls import path
from . import views

urlpatterns= [
    path('',views.home,name="home"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('register',views.register,name="register"),
    path('catagory',views.catagory,name="catagory"),
    path('cart',views.cart,name="cart"),
    path('heart',views.heart,name="heart"),
    path('heart_page',views.heart_page,name="heart_page"),
    path('catagory/<str:name>',views.catagoryview,name="catagory"),
    path('catagory/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('addcart',views.add_cart,name="addcart"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('remove_heart/<str:hid>',views.remove_heart,name="remove_heart"),
    path('search_product',views.search_product,name="search_product"),
    path('searchview',views.searchview,name="searchview"),
]