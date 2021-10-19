from .models import *
from django import forms


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'description', 'categorie', 'date']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categorie': forms.Select(attrs={'class': 'form-control'})
        }


