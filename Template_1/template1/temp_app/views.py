from django.shortcuts import render
import datetime
# Create your views here.
def show(request):
    return render(request,'temp_app/index.html')

def display(request):
    date=datetime.datetime.now()
    dict={'date':date}
    return render(request,'temp_app/time.html',context=dict)

def display1(request):
    date=datetime.datetime.now()
    name='djnago'
    fees=25000
    dict={'date':date,'name':name,'fees':fees}
    return render(request,'temp_app/context1.html',context=dict)
import random
def display2(request):
    date=datetime.datetime.now()
    msg_list=['hello dear','miss you','kill you','good morning']
    name_list=['supriya','rajendra','ajit','gitanjali']
    name=random.choice(name_list)
    msg=random.choice(msg_list)
    dict={'date':date,'name':name,'msg':msg}
    return render(request,'temp_app/context2.html',context=dict)

def display3(request):
    date=datetime.datetime.now()
    msg='hello guest good'
    h=date.hour
    if h<12:
        msg+="good morning"
    elif h<16:
        msg+="good afternoon"
    elif h<21:
        msg+="good evening"
    else: 
        msg+="good night"
    dict={'date':date,'msg':msg}
    return render(request,'temp_app/context3.html',dict)