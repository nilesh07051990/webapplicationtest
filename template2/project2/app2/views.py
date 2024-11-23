from django.shortcuts import render
import datetime
import random
from app2.models import Employee
from app2.forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def display(request):
    return render(request,'app2/wish.html')


def show(request):
    date=datetime.datetime.now()
    name='django'
    qualification='Btech'
    dict={'date':date,'name':name,'qualification':qualification}
    return render(request,'app2/index.html',dict)

def show1(request):
    date=datetime.datetime.now()
    msg_list=[
        'hello how are you',
        'hello i miss you',
        'hello sweetheart',
        'good bye'
    ]
    name_list=['nilesh','ankita','raju','nikhil']
    name=random.choice(name_list)
    msg=random.choice(msg_list)
    h=date.hour
    if h<12:
        msg+=' good morning'
    elif h<16:
        msg+=' afternoon'
    elif h<21:
        msg+=' evening'
    else:
        msg='hello guest, very good night'
    dict={'date':date,'name':name,'msg':msg}
    return render(request,'app2/random_from_list.html',dict)

def movies(request):
    head_message='welcome to movie portal'
    m1='salman khan break up with katrina'
    m2='jawan movie can release in september'
    m3='dipika padukon is pregnant'
    my_dict={'head_message':head_message,'m1':m1,'m2':m2,'m3':m3}
    return render(request,'app2/news.html',context=my_dict)

@login_required
def table_view(request):
    emp_list=Employee.objects.all()
    dict={'emp_list':emp_list}
    return render(request,'app2/emp.html',dict)


def forminputform(request):
    submitted=False
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            print("form validation successful and printing data")
            print("name:",form.cleaned_data['name'])
            print("marks:",form.cleaned_data['marks'])
            submitted=True
        else:
            print("some fieldvalidations fail")
    form=StudentForm()
    dict={'form':form,'submitted':submitted}
    return render(request,'app2/input.html',dict)

def logout_view(request):
    logout(request)  # Log out the user
    return render(request,'app2/logout.html')
