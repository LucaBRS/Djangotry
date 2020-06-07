from django.db import models

# Create your models here.



class Article(models.Model):
    #questo è un modello e bisogna dare la MIGRAZIONE
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add thumbani
    # autore


#### how to do migrations   ####
    # manage.py makemigration
    # manage.py migrate