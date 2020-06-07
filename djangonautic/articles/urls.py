####IMPORTANTE registrare l'app allinterno di settings del main project

# copiato incollato da urls di djangonautic

from django.conf.urls import url
from django.urls import path
from . import views            
 # . same dir

urlpatterns = [
    
    url(r'^$',views.article_list),
]
