from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.db import transaction
from .models import *
from .forms import *

# Type 2 means with submenu, type 1 means without submenu.
top_menu = [
{
    'type': '2',
    'title': 'For Youth', 
    'link': 'index',
    'sub_menu': [
        {
            'title': 'Voluntary projects', 
            'link': 'gv'
        },
        {
            'title': 'Internships at start-ups', 
            'link': 'ge'
        },
        {
            'title': 'Professional internships', 
            'link': 'gt'
        },
        {
            'title': 'Join AIESEC', 
            'link': 'join_aiesec'
        }
        ] 
},

{
    'type': '2',
    'title': 'Offices', 
    'link': 'offices',
    'sub_menu': [       
        {
            'title': 'All Offices', 
            'link': 'offices'
        },
        {
            'title': 'AIESEC in Algeria', 
            'link': 'AiA'
        },
        {
            'title': 'AIESEC in Babez', 
            'link': 'babez'
        },
        {
            'title': 'AIESEC in Benak', 
            'link': 'benak'
        },
        {
            'title': 'AIESEC in Blida', 
            'link': 'blida'
        },
        {
            'title': 'AIESEC in Constantine', 
            'link': 'cons'
        },
        {
            'title': 'AIESEC in Oran', 
            'link': 'oran'
        },
        {
            'title': 'AIESEC in Ouargla', 
            'link': 'ouargla'
        }
        ] 
},
{
    'type': '2',
    'title': 'Events', 
    'link': 'index',
    'sub_menu': [
        {
            'title': 'Youth Speak Forum',
            'link': 'ysf'
        },
        {
            'title': 'Global Village',
            'link': 'globalv'
        }
    ]
},


{
  'type': '1',
  'title' : 'Y4GG',
  'link' : 'y4gg'    
},

{
  'type': '1',
  'title' : 'Host family',
  'link' : 'host_family'    
},
]
def index(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/index.html', context)

def companies(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/companies.html', context)

def offices(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/offices.html', context)

def gv(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/gv.html', context)

def ge(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/ge.html', context)

def gt(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/gt.html', context)

def testimonials(request):
    form = TestimonialForm()
    context = {'top_menu':top_menu, 'form': form}
    return render(request, 'main/testimonials.html', context)

def join_aiesec(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/join_aiesec.html', context)

def host_family(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/host_family.html', context)

def contact(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/contact.html', context)

def ysf(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/ysf.html', context)

def y4gg(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/y4gg.html', context)

def cookies(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/cookies.html', context)

def babez(request):
    context = {'top_menu':top_menu}
    return redirect('babez/')

def benak(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/benak.html', context)

def blida(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/blida.html', context)

def oran(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/oran.html', context)

def cons(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/cons.html', context)

def ouargla(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/ouargla.html', context)

def blog(request):
    context = {'top_menu':top_menu}
    return redirect(request, 'http:www.blog.aiesec.dz', context)

def globalv(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/globalv.html', context)

def AiA(request):
    context = {'top_menu':top_menu}
    return render(request, 'main/AiA.html', context)