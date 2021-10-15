from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import *


def home(request):
    return render(request, 'home.html')


def liste_articles(request):
    queryset = Article.objects.all()
    context = {
        'articles': queryset
    }

    return render(request, 'liste-article.html', context)


def ajout_article(request):
    form = ArticleModelForm()
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(liste_articles)
        else:
            messages.error(request, "verifiez les informations saisies svp !")
    context = {'form': form}
    return render(request, 'ajout-article.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})
