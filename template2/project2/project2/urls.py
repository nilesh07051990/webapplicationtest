"""
URL configuration for project2 project.

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
from django.contrib.auth import views as auth_views
from django.urls import path,include
from app2 import views as v1
from accountapp import views as v2
from employee import views as v3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v1.display),
    path('display2/', v1.show),
    path('display3/', v1.show1),
    path('movies1/', v1.movies),
    path('emps/', v1.table_view),
    path('forms/',v1.forminputform),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', v1.logout_view, name='logout'),
    path('accnt/',v2.account_view),
    path('form1/',v2.account_form),
    path('curd1/',v3.show_view,name='show_view'),
    path('insert/',v3.Create)



]
