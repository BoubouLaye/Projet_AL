# Generated by Django 3.2.8 on 2021-10-20 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_article_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categorie',
            field=models.CharField(choices=[('sport', 'sport'), ('sante', 'sante'), ('politique', 'politique')], max_length=30),
        ),
    ]
