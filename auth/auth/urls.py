from django.contrib import admin  
from django.urls import path  
from authapp import views  
 
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('',views.index),
    path('login/',views.login),
    path('home/',views.home),
]  