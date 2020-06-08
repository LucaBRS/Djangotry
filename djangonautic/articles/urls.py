####IMPORTANTE registrare l'app allinterno di settings del main project

# copiato incollato da urls di djangonautic

from django.conf.urls import url
from django.urls import path
from . import views            
 # . same dir


app_name= 'articles' #questo è per distingruere i nomi!!! cosi da fare articles:list o altro

urlpatterns = [
    
    url(r'^$',views.article_list, name = "list"),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail, name = "detail"),  #questo è il modo per prendere la quesry nell url e passarla al "server"
    
]
