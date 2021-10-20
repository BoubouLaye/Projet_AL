from django.contrib import admin
from django.urls import path,include
path('accounts/', include('django.contrib.auth.urls')),
from App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup', signup, name='signup'),
    path('articles', liste_articles, name='articles'),
    path('categorie/<str:cat>', categorie_view, name='categorie'),
    path('articles/telechargement', download, name='download'),
    path('articles/ajout', ajout_article, name='ajout_article'),
    path('articles/delete/<int:pk>', delete_article, name='delete_article'),
    path('accounts/', include('django.contrib.auth.urls')),

]
