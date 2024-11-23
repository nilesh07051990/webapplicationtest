from django.shortcuts import render
from accountapp.models import CreateAccount
from.form import CreateAccountForm
from dataclasses import fields

# Create your views here.
def account_view(request):
    #accounts = CreateAccount.objects.all()
    accounts=CreateAccount.objects.filter(salary__gt=5000)
    print(accounts)
    return render (request, 'accountapp/account.html',{'accounts':accounts})
  


def account_form(request):
    form= CreateAccountForm()

    if request.method =='POST':
        form=CreateAccountForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form= CreateAccountForm()

    return render(request,'accountapp/orm.html',{'form':form})