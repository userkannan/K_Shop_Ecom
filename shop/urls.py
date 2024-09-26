from django.urls import path
from . import views

urlpatterns= [
    path('',views.home,name="home"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('register',views.register,name="register"),
    path('catagory',views.catagory,name="catagory"),
    path('catagory/<str:name>',views.catagoryview,name="catagory"),
    path('catagory/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('addcart',views.add_cart,name="addcart"),
]