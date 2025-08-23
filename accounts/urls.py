from django.urls import path
from . import views


app_name = "accounts"


urlpatterns = [
path("register/", views.register, name="register"),
path("profile/", views.profile, name="profile"),
path("login/", views.login_view, name="login"),
path("logout/", views.logout_view, name="logout"),
path("addresses/", views.address_list, name="address_list"),
path("addresses/add/", views.address_create, name="address_create"),
path("addresses/<int:pk>/edit/", views.address_update, name="address_update"),
path("addresses/<int:pk>/delete/", views.address_delete, name="address_delete"),
]