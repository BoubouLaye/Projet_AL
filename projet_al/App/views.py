from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib.auth.decorators import login_required


def home(request):
    last = Article.objects.all().order_by('-date')[:5]
    context = {
        'articles': last
    }
    return render(request, 'home.html', context)


def download(request):
    queryset = Article.objects.all()
    context = {
        'articles': queryset
    }

    return render(request, 'download.html', context)


def categorie_sante(request):

    liste_article = Article.objects.filter(categorie="sante")
    context = {'liste_articles': liste_article}
    return render(request, 'categorie-sante.html', context)

def categorie_sport(request):

    liste_article = Article.objects.filter(categorie="sport")
    context = {'liste_articles': liste_article}
    return render(request, 'categorie-sport.html', context)

def categorie_politique(request):

    liste_article = Article.objects.filter(categorie="politique")
    context = {'liste_articles': liste_article}
    return render(request, 'categorie-sante.html', context)


def liste_articles(request):
    queryset = Article.objects.all()
    context = {
        'articles': queryset
    }

    return render(request, 'liste-article.html', context)

def detail_article(request,pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article
    }

    return render(request, 'detail-article.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def delete_article(request,pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect(liste_articles)

@login_required(login_url='login')
def edit_article(request,pk):
    article = Article.objects.get(id=pk)
    form = ArticleModelForm(instance=article)
    context = {'form': form}
    if request.method == 'POST':
        form = ArticleModelForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect(liste_articles)

    return render(request, 'update-article.html', context=context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
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
