from django.shortcuts import render, redirect
from django.forms import ModelForm
from .forms import CreateUserForm

# Create your views here.
def index(request):
    return render(request, 'Register/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        print("Invalid detals, Try again")
        form = CreateUserForm()
    context = {'form': CreateUserForm()}
    return render(request, 'Register/register.html', context)

def login(request):
    return render(request, 'Register/login.html')
    
   