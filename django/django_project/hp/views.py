from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

Reqs=[
    {
        'NGOName':'A1',
        'Loc':'Madhya Pradesh',
        'Requirement':'10 Beds',
        'date_posted':'Sept 27, 2020'
     },
     {
        'NGOName':'B2',
        'Loc':'Goa',
        'Requirement':'50 Syringes',
        'date_posted':'Sept 19, 2020'
      }
]


def home(request): 
    context = {
        'Reqs':Reqs
        }
    return render(request, 'hp/home1.html',context)
 

def about(request):
    return render(request, 'hp/about.html', {'title':'About'})

