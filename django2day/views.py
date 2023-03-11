from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from .models import Customer

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def django2day(request):
    mydjango2day=Customer.objects.all().values()
    template=loader.get_template('customers.html')
    context={
        'mydjango2day':mydjango2day,
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    mydjango2day=Customer.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'mydjango2day':mydjango2day,
    }
    return HttpResponse(template.render(context,request))
