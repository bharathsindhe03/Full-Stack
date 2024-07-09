"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from myApp1.views import current_time
from myApp2.views import offset_increase,offset_decrease
from myApp3.views import lists
from myApp4.views import home, contactus,aboutus

urlpatterns = [
    #app1
    path('time/',current_time),

    #app2
    path('time1/<int:offset>',offset_increase),
    path('time2/<int:offset>',offset_decrease),
    
    #app3
    path('lists/',lists),

    #app4
    path('home/',home),
    path('contactus/',contactus),
    path('aboutus/',aboutus),

    path('admin/', admin.site.urls),
]
