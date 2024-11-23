"""
URL configuration for template1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from temp_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show1/', views.show),
    path('display1/', views.display),
    path('display2/', views.display1),
    path('display3/', views.display2),
    path('display4/', views.display3),
    
    

]
