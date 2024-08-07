from django.urls import path

from myapp.views import register, profile, add_pass, index, pass_verify


urlpatterns = [
    path("", index, name="index"),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('add_pass/', add_pass, name='add_pass'),
]