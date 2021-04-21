from django.shortcuts import render, redirect, HttpResponse
from .models import Dojo,Ninja
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'dojos':Dojo.objects.all(),
        'ninjas':Ninja.objects.all()
    }
    return render(request,'index.html',context )



def create_ninja(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    dojo=request.POST['dojo_name']
    Ninja.objects.create(
        first_name=first_name,
        last_name=last_name,
        dojo_id=dojo
    )
    return redirect('/')

def create_dojo(request):
    dojo=Dojo.objects.all()
    name=request.POST['name']
    city=request.POST['city']
    state=request.POST['state']
    Dojo.objects.create(
        name=name,
        city=city,
        state=state
    )
    return redirect('/')