from django.urls import path

from myapp.views import register, profile, add_pass, index , logout_passenger


urlpatterns = [
    path("", index, name="index"),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('add_pass/', add_pass, name='add_pass'),
    path('accounts/logout_passenger/', logout_passenger, name='logout_passenger'),
]