from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def indexView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')

def homeView(request):
    if request.user.is_authenticated==False:
        return redirect('login')
    return render(request, 'index.html')

def leadCreateView(request):
    if request.user.is_authenticated==False:
        return redirect('login')
    return render(request, 'lead_create.html')

def firstMeetingView(request):
    if request.user.is_authenticated==False:
        return redirect('login')
    return render(request, 'first_meeting.html')

def convertedView(request):
    if request.user.is_authenticated==False:
        return redirect('login')
    return render(request, 'converted.html')

def closedView(request):
    if request.user.is_authenticated==False:
        return redirect('login')
    return render(request, 'closed.html')

def meetingsView(request):
    if request.user.is_authenticated==False:
        return redirect('login')
    return render(request, 'meetings.html')

def statusUpdateView(request):
    if request.user.is_authenticated==False:
        return redirect('login')
    return render(request, 'status_update.html')

def leadConvertedView(request):
    if request.user.is_authenticated==False:
        return redirect('login')
    return render(request, 'lead_converted.html')

def leadClosedView(request):
    if request.user.is_authenticated==False:
        return redirect('login')
    return render(request, 'lead_closed.html')

def meetingCreateView(request):
    if request.user.is_authenticated==False:
        return redirect('login')
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