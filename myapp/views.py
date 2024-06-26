from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, AddPassForm
from .models import Passenger, Pass, Bus
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

# View for user registration
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'buspass/register.html', {'form': form})

# View for displaying the user's profile
@login_required
def profile(request):
    try:
        passenger = request.user.passenger_profile
        passes = passenger.passes.all()
        return render(request, 'buspass/profile.html', {'passenger': passenger, 'passes': passes})
    except Passenger.DoesNotExist:
        # Handle case where the user does not have a Passenger profile
        return render(request, 'buspass/profile.html', {'passenger': None, 'passes': None})

# View for adding a new bus pass
@login_required
def add_pass(request):
    if request.method == 'POST':
        form = AddPassForm(request.POST)
        if form.is_valid():
            new_pass = form.save(commit=False)
            new_pass.passenger = request.user.passenger_profile
            new_pass.save()
            return redirect('profile')
    else:
        form = AddPassForm()
    return render(request, 'buspass/add_pass.html', {'form': form})