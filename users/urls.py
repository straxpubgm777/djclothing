from django.urls import path
from users.views import *

urlpatterns = [
    path('login/', login, name="login_url"),
    path('logout/',signout,name="logout_url")
]