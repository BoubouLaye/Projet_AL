from django.contrib import admin
from django.urls import path,include
path('accounts/', include('django.contrib.auth.urls')),
from App.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup', signup, name='signup'),
    path('articles', liste_articles, name='articles'),
    path('articles/sante', categorie_sante,name='sante' ),
    path('articles/sport', categorie_sport, name='sport'),
    path('articles/politique', categorie_politique,name='politique' ),
    path('articles/telechargement', download, name='download'),
    path('articles/ajout', ajout_article, name='ajout_article'),
    path('articles/delete/<int:pk>', delete_article, name='delete_article'),
    path('articles/detail/<int:pk>', detail_article, name='detail'),
    path('articles/edit/<int:pk>', edit_article, name='edit_article'),
    path('accounts/', include('django.contrib.auth.urls')),

]
