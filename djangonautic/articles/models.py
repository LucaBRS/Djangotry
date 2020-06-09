from django.db import models

# Create your models here.



class Article(models.Model):
    #questo è un modello e bisogna dare la MIGRAZIONE
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True) #per ogni cambiamento si da la migrazione
    # autore


#### how to do migrations   ####
    # manage.py makemigration
    # manage.py migrate

    def __str__(self):
         return self.title

    def snippet(self):
        return self.body[0:50] + '...'