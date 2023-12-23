from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random
# Create your views here.
times = 0
def dice(request):
    no = random.randint(1,6)
    return render(request,"dice.html",{"no":no})
def dice2(request):
    no1 = random.randint(1,6)
    no2 = random.randint(1,6)
    no3 = random.randint(1,6)
    return render(request,"dice2.html",locals())
def dice3(request):
    global times
    times += 1
    local_times = times
    username = "kevinfir"
    dict_no = {"no":random.randint(1,6)}
    return render(request,"dice3.html",locals())
