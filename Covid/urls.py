"""Covid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from covid19app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('main/',views.main, name='main'),
    path('base/',views.base),
    path('temp/',views.temp, name='p1'),  
    path('temp2/',views.temp2, name='p2'),
    path('temp3/',views.temp3, name='p3'),
    path('temp4/',views.temp4, name='p4'),
    path('temp5/',views.temp5, name='p5'),
    path('temp6/',views.temp6, name='p6'),
    path('temp7/',views.temp7, name='p7'),
    path('predict/',views.predict, name="pred")
]
