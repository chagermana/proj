from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from .models import Customer
from .forms import InputForm
from .forms import BeginningForm
from django.http import HttpResponseRedirect

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

def home_view(request):
    context={}
    context['form']=InputForm()
    return render(request,"sign in.html",context)

def hi(request):
    context={}
    context['form']=InputForm()
    return render(request,"sign up.html",context)

def beginning(request):
    submitted=False
    if request.method=="POST":
        form = BeginningForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/beginning?submitted=True')
    else:
        form=BeginningForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,"beginning.html",{'form':form,'submitted':submitted})


