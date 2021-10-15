from django.contrib import admin
from django.urls import path
from App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup', signup, name='signup'),
    path('login', login, name='login')
]
