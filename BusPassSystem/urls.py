"""
URL configuration for BusPassSystem project.

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
from django.urls import path, include

from myapp.views import logout_passenger


urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", include("myapp.urls")),
    path('buspass/', include('myapp.urls')),
    path('verify/', include('myapp.verify_urls')),
    # path('verify/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout_passenger/', logout_passenger, name='logout_passenger'),
]

# /accounts/login/,
# /accounts/logout/, 
# /accounts/password_change/

# from django.contrib import admin
# from django.urls import path, include
# 
# urlpatterns = [
    # path('admin/', admin.site.urls),
    # # path("index/", include("myapp.urls")),
    # path('buspass/', include('myapp.urls')),
    # path('accounts/', include('django.contrib.auth.urls')), 
# ]
# 