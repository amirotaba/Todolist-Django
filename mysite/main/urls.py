from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name='login'),
    path("logout/", views.logout_request, name='logout'),
    path("resetpassword", views.resetpassword_request, name="resetpassword"),
    path("getanswer", views.getanswer_request, name="getanswer"),
    path("setnewpassword", views.setnewpassword_request, name="setnewpassword"),
]
