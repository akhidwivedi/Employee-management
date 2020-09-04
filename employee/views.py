from django.shortcuts import render,redirect
from .forms import EmployeeForm,UserLoginForm
from .models import employee





def employee_list(request):
    context ={'employee_list': employee.objects.all()}
    return render(request,"employee/employee_list.html",context)


def employee_forms(request,id=0):
    if request.method== "GET":
        if id==0:
            form =EmployeeForm()
        else:
            employees= employee.objects.get(pk=id)
            form = EmployeeForm(instance=employees)    
        return render(request,"employee/employee_forms.html",{'form':form})
    # if request.method == "POST":
    else:
 
        if id==0:
            form=EmployeeForm(request.POST)
        else:
            employees= employee.objects.get(pk=id)
            form= EmployeeForm(request.POST,instance= employees)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request,id):
    employees= employee.objects.get(pk=id)
    employees.delete()
    return redirect('/employee/list')

