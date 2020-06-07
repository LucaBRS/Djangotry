#prima cosa è importare
from django.http import HttpResponse
from django.shortcuts import render



###!!!! andare dentro settings e cercare per TEMPLATES nella sezione DIRS mettere la 'directory' delle pagine 

def homepage(request):
   # return HttpResponse('homepage')
   #retorn template e importiamo il modulo per reder
   return render(request,'homepage.html')

def about(request):
    #return HttpResponse('about')
     #retorn template e importiamo il modulo per reder
    return render(request,'about.html')

def project(request):
    return render(request,'./www/index.html')