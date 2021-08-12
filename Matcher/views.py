from django.shortcuts import render
from django.http import HttpResponse, response
# from .models import adi
def home(request):
 return(render(request, 'Matcher/home.html'))


