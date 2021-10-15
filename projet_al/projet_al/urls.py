from django.contrib import admin
from django.urls import path,include
path('accounts/', include('django.contrib.auth.urls')),
from App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),

]
