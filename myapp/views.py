from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, AddPassForm
from .models import Passenger, Pass, Bus
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

def index(request):
    return render(request, 'index.html')

def logout_passenger(request):
    auth_logout(request)
    return render(request, 'registration/logout.html')

def pass_verify(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        bus_number = request.POST.get("bus_number")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                bus = Bus.objects.get(bus_number=bus_number)
                passenger = user.passenger_profile
                passes = passenger.passes.filter(bus=bus)
                return render(request, "verify/pass_verify.html", {"passenger": passenger, "passes": passes})
            except Bus.DoesNotExist:
                return render(request, "verify/pass_verify.html", {"error": "Invalid bus number"})
        else:
            return render(request, "verify/pass_verify.html", {"error": "Invalid username or password"})
    return render(request, "verify/pass_verify.html")

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