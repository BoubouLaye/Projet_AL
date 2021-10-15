from django.db import models
from django.utils import timezone


class Article(models.Model):
    titre = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    date = models.DateTimeField(default=timezone.now, blank=True)
    cat_choises = (
        ('Sport', 'Sport'),
        ('sante', 'Santé'),
        ('Politique', 'Politique'),

    )
    categorie = models.CharField(max_length=30, choices=cat_choises)
