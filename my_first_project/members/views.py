from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

# Create your views here.
def hello(request):
    template = loader.get_template('hello.html')
    return HttpResponse(template.render())

all_members = Member.objects.all().values()

def all_member(request):
    template = loader.get_template('all_member.html')
    context = {
        'members': all_members,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'member': member,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'members': all_members,
        'fruits': ['Banana', 'Orange', 'Mango', 'Kiwi'],
    }
    return HttpResponse(template.render(context, request))

def testing2(request):
    # firstNames = Member.objects.filter(Q(firstName__contains='i') | Q(id=2)).values()
    firstNames = Member.objects.all().order_by('-firstName').values()
    template = loader.get_template('template2.html')
    context = {
        'firstNames': firstNames,
    }
    return HttpResponse(template.render(context, request))