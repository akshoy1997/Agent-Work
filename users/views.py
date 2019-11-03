from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def indexView(request):
    return redirect('login')

@login_required()
def homeView(request):
    return render(request, 'index.html')

@login_required()
def leadCreateView(request):
    return render(request, 'lead_create.html')

@login_required()
def convertedView(request):
    return render(request, 'converted.html')

@login_required()
def closedView(request):
    return render(request, 'closed.html')

@login_required()
def meetingsView(request):
    return render(request, 'meetings.html')

@login_required()
def statusUpdateView(request):
    return render(request, 'status_update.html')

@login_required()
def meetingCreateView(request):
    return render(request, 'meeting_create.html')

def registerView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})