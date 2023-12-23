from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random
# Create your views here.
def show(request):
    no = random.randint(1,6)
    return render(request,"dice.html",{"no":no})