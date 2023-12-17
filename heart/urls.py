from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("predict", views.predict, name="predict"),
]
