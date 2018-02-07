from django.shortcuts import render
from recordapp.form import Postform
# from recordapp.models import record



def index(request):
    postform = Postform()
    return render(request,"index.html",locals())
# Create your views here.


def new(request):
    postform = Postform()
    return render(request,"new.html",locals())
