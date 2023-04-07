from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Emp
from .forms import EmpForm
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# def emp_main(request):
#     response_data = render_to_string('home.html')
#     return HttpResponse(response_data)
@login_required
def emp_list(request):
    emps=Emp.objects.all()
    return render(request,'emp_list.html',{'emps':emps})
@login_required
def emp_create(request):
    if request.method=='POST':
        form=EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form=EmpForm()
    return render(request,'emp_form.html',{'form':form})
@login_required
def emp_update(request,pk):
    empl=get_object_or_404(Emp,pk=pk)
    if request.method=='POST':
        form=EmpForm(request.POST,instance=empl)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form=EmpForm(instance=empl)
    return render(request,'emp_form.html',{'form':form})
@login_required
def emp_delete(request,pk):
    empl=get_object_or_404(Emp,pk=pk)
    empl.delete()
    return redirect('emp_list')

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('emp_list')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})
def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('emp_list')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout(request):
    auth_logout(request)
    return redirect('login')