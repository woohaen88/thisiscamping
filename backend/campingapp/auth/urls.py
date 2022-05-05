from django.urls import path
from campingapp.auth.views import signin, signup


app_name = "auth"

urlpatterns = [
    path("signin", signin, name="signin"),
    path("signup", signup, name="signup"),
]
