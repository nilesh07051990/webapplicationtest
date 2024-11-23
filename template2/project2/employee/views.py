from django.shortcuts import render,redirect
from .models import Employee
from.form import EmployeeForm

# Create your views here.
def show_view(request):
    employee= Employee.objects.all()
    return render(request,'employee/index.html',{'employee':employee})

# View to create a new employee
def Create(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = EmployeeForm()
            return redirect('show_view')
    return render(request, 'employee/create.html', {'form': form})