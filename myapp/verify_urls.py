from django.urls import path

from myapp.views import index, pass_verify


urlpatterns = [
    path("", index, name="index"),
    path('pass_verify/', pass_verify, name='pass_verify'),
]