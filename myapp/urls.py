from django.urls import path
from myapp.views import register, profile, add_pass, index

urlpatterns = [
    path("", index, name="index"),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('add_pass/', add_pass, name='add_pass'),
]



# from django.urls import path

# from myapp.views import register,profile,add_pass

# from . import views

# urlpatterns = [
#     # path("", index, name="index"),
#     path('register/', register, name='register'),
#     path('profile/', profile, name='profile'),
#     path('add_pass/', add_pass, name='add_pass'),
# ]