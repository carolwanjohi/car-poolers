from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Driver, DriverProfile, Passenger, PassengerProfile
from .forms import NewDriver, DriverLogin, UpdateDriverProfile, NewPassenger, PassengerLogin, UpdatePassengerProfile
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
# from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    '''
    View function for the landing page of the application
    '''
    title = 'CarPoolers'
    message = 'Landing Page'
    return render(request,'index.html',{"title":title,"message":message})

def new_driver(request):
    '''
    View function to display a registration form when the user selects the driver option
    '''
    title = 'Sign Up Driver'

    if request.method == 'POST':

        form = NewDriver(request.POST)

        if form.is_valid:

            first_name = request.POST.get('first_name')

            last_name = request.POST.get('last_name')

            phone_number = request.POST.get('phone_number')

            new_driver = Driver(first_name=first_name, last_name=last_name, phone_number=phone_number)

            new_driver.save()

            return redirect(driver, new_driver.id)

        else:

            messages.error(request, ('Please correct the error below.'))

    else:

        form = NewDriver()

        return render(request, 'registration/driver/registration_form.html', {"title":title, "form":form})

def driver_login(request):
    '''
    View function to display login form for a driver
    '''
    title = "Sign In Driver"

    if request.method == 'POST':

        form = DriverLogin(request.POST)

        if form.is_valid:

            phone_number = request.POST.get('phone_number')

            try:
                found_driver = Driver.objects.get(phone_number=phone_number)

                return redirect(driver, found_driver.id)

            except ObjectDoesNotExist:
                raise Http404()

        else:

            messages.error(request, ('Please correct the error below.'))

    else:
        form = DriverLogin()

        return render(request, 'registration/driver/login.html',{"title":title,"form":form})

@login_required(login_url='/new/driver/')
def driver(request, id):
    '''
    View function to display an authenticated logged in driver's profile
    '''

    driver = Driver.objects.get(id=id)

    title = f'{driver.first_name} {driver.last_name}'

    driver_profile = DriverProfile.objects.get(driver=driver)

    return render(request, 'all-drivers/profile.html', {"title":title, "driver":driver, "driver_profile":driver_profile})

@login_required(login_url='/new/driver/')
@transaction.atomic
def update_driver_profile(request, id):
    '''
    View function to display an update driver profile form for an authenticated driver
    '''

    found_driver = Driver.objects.get(id=id)

    title = f'Update Profile'

    if request.method == 'POST':

        # driver_form = NewDriver(request.POST)

        driver_profile_form = UpdateDriverProfile(request.POST, instance=found_driver.driverprofile,files=request.FILES)

        if  driver_profile_form.is_valid():

            # driver_details = driver_form.save(commit=False)

            driver_profile = driver_profile_form.save(commit=False)

            driver_profile.driver = found_driver

            driver_profile.profile_pic = driver_profile_form.cleaned_data['profile_pic']

            driver_profile.car_image = driver_profile_form.cleaned_data['car_image']

            driver_profile.save()

            # driver_details.save()


            return redirect(driver, found_driver.id)

        else:

            messages.error(request, ('Please correct the error below.'))

    else:

        # driver_form = NewDriver(instance=found_driver)

        driver_profile_form = UpdateDriverProfile(instance=found_driver.driverprofile)

        return render(request, 'all-drivers/update-profile.html', {"title":title,"driver":found_driver,"driver_profile_form":driver_profile_form})

def new_passenger(request):
    '''
    View function to display a registration form when the user selects the passenger option
    '''
    title = 'Sign Up Passenger'

    if request.method == 'POST':

        form = NewPassenger(request.POST)

        if form.is_valid:

            first_name = request.POST.get('first_name')

            last_name = request.POST.get('last_name')

            phone_number = request.POST.get('phone_number')

            new_passenger = Passenger(first_name=first_name, last_name=last_name, phone_number=phone_number)

            new_passenger.save()

            return redirect(passenger, new_passenger.id)

        else:

            messages.error(request, ('Please correct the error below.'))

    else:

        form = NewPassenger()

        return render(request, 'registration/passenger/registration_form.html', {"title":title, "form":form})

def passenger_login(request):
    '''
    View function to display login form for a passenger
    '''
    title = "Sign In Passenger"

    if request.method == 'POST':

        form = PassengerLogin(request.POST)

        if form.is_valid:

            phone_number = request.POST.get('phone_number')

            try:
                found_passenger = Passenger.objects.get(phone_number=phone_number)

                return redirect(passenger, found_passenger.id)

            except ObjectDoesNotExist:
                raise Http404()

        else:

            messages.error(request, ('Please correct the error below.'))

    else:
        form = PassengerLogin()

        return render(request, 'registration/passenger/login.html',{"title":title,"form":form})


@login_required(login_url='/new/passenger/')
def passenger(request, id):
    '''
    View function to display an authenticated logged in passenger's profile
    '''

    passenger = Passenger.objects.get(id=id)

    title = f'{passenger.first_name} {passenger.last_name}'

    passenger_profile = PassengerProfile.objects.get(passenger=passenger)

    return render(request, 'all-passengers/profile.html', {"title":title, "passenger":passenger, "passenger_profile":passenger_profile})

@login_required(login_url='/new/passenger/')
@transaction.atomic
def update_passenger_profile(request, id):
    '''
    View function to display an update passenger profile form for an authenticated passenger
    '''

    found_passenger = Passenger.objects.get(id=id)

    title = f'Update Profile'

    if request.method == 'POST':

        # passenger_form = NewPassenger(request.POST)

        passenger_profile_form = UpdatePassengerProfile(request.POST, instance=found_passenger.passengerprofile,files=request.FILES)

        if passenger_profile_form.is_valid():

            # passenger_details = passenger_form.save(commit=False)

            passenger_profile = passenger_profile_form.save(commit=False)

            passenger_profile.passenger = found_passenger

            passenger_profile.profile_pic = passenger_profile_form.cleaned_data['profile_pic']

            passenger_profile.save()

            # passenger_details.save()


            return redirect(passenger, found_passenger.id)

        else:

            messages.error(request, ('Please correct the error below.'))

    else:

        # passenger_form = NewPassenger(instance=found_passenger)

        passenger_profile_form = UpdatePassengerProfile(instance=found_passenger.passengerprofile)

        return render(request, 'all-passengers/update-profile.html', {"title":title,"passenger":found_passenger,"passenger_profile_form":passenger_profile_form})





