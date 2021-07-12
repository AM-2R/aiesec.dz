from django.shortcuts import render
from django.views import generic

def home_page(request):
    return render(request, 'babez/index.html')

def algiers(request):
    return render(request, 'babez/algiers.html')

def local_committee(request):
    return render(request, 'babez/lc.html')
