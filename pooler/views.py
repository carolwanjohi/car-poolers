from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Driver, DriverProfile, Passenger, PassengerProfile, DriverReview, PassengerReview, TravelPlan
from .forms import NewDriver, DriverLogin, UpdateDriverProfile, NewPassenger, PassengerLogin, UpdatePassengerProfile, ReviewDriverForm, ReviewPassengerForm
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

# Driver registration and log in
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

# Drive homepage is Profile page
@login_required(login_url='/new/driver/')
def driver(request, id):
    '''
    View function to display an authenticated logged in driver's profile
    '''

    driver = Driver.objects.get(id=id)

    title = f'{driver.first_name} {driver.last_name}'

    driver_profile = DriverProfile.objects.get(driver=driver)

    return render(request, 'all-drivers/profile.html', {"title":title, "driver":driver, "driver_profile":driver_profile})

# Driver update profile
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

# Passenger registration and log in
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

# Passenger homepage is Profile page
@login_required(login_url='/new/passenger/')
def passenger(request, id):
    '''
    View function to display an authenticated logged in passenger's profile
    '''

    passenger = Passenger.objects.get(id=id)

    title = f'{passenger.first_name} {passenger.last_name}'

    passenger_profile = PassengerProfile.objects.get(passenger=passenger)

    return render(request, 'all-passengers/profile.html', {"title":title, "passenger":passenger, "passenger_profile":passenger_profile})

# Passenger update profile 
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

# Passenger see list of drivers
@login_required(login_url='/new/passenger/')
def drivers(request,id):
    '''
    View function to display list of driver profiles
    '''
    passenger = Passenger.objects.get(id=id)

    title = "Driver Reviews"

    driver_profiles = DriverProfile.objects.all()

    return render(request, "all-passengers/reviews.html", {"title":title,"passenger":passenger, "driver_profiles":driver_profiles})

# Passenger see selected driver's profile and reviews
@login_required(login_url='/new/passenger/')
def driver_profile(request, passenger_id, driver_profile_id):
    '''
    View function to display list of driver profiles
    '''
    passenger = Passenger.objects.get(id=passenger_id)

    driver_profile = DriverProfile.objects.get(id=driver_profile_id)

    title = f'{driver_profile.driver.first_name} {driver_profile.driver.last_name}\'s Profile'

    reviews = DriverReview.get_driver_reviews(driver_profile_id)

    form = ReviewDriverForm()

    return render(request, "all-passengers/driver-profile.html", {"title":title, "passenger":passenger, "driver_profile":driver_profile, "reviews":reviews, "form":form})

# Passenger create a driver review
def review_driver(request, passenger_id, driver_profile_id):
    '''
    Function that saves a driver review without reloading the page
    '''
    passenger = Passenger.objects.get(id=passenger_id)

    driver_profile = DriverProfile.objects.get(id=driver_profile_id)

    review_content = request.POST.get('review_content')

    new_driver_review = DriverReview(passenger=passenger, driver_profile=driver_profile, review_content=review_content )

    new_driver_review.save()

    data = {'success':'Your review has successfully been saved'}

    return JsonResponse(data)

# Driver see lis of passengers
@login_required(login_url='/new/passenger/')
def passengers(request,id):
    '''
    View function to display list of passenger profiles
    '''
    driver = Driver.objects.get(id=id)

    title = "Passenger Reviews"

    passenger_profiles = PassengerProfile.objects.all()

    return render(request, "all-drivers/reviews.html", {"title":title,"driver":driver, "passenger_profiles":passenger_profiles})

# Driver see selected passenger's profile and reviews
@login_required(login_url='/new/passenger/')
def passenger_profile(request, driver_id, passenger_profile_id):
    '''
    View function to display list of driver profiles
    '''
    driver = Driver.objects.get(id=driver_id)

    passenger_profile = PassengerProfile.objects.get(id=passenger_profile_id)

    title = f'{passenger_profile.passenger.first_name} {passenger_profile.passenger.last_name}\'s Profile'

    reviews = PassengerReview.get_passenger_reviews(passenger_profile_id)

    form = ReviewPassengerForm()

    return render(request, "all-drivers/passenger-profile.html", {"title":title, "driver":driver, "passenger_profile":passenger_profile, "reviews":reviews, "form":form})

# Driver create a passenger review
def review_passenger(request, driver_id, passenger_profile_id):
    '''
    Function that saves a passenger review without reloading the page
    '''
    driver = Driver.objects.get(id=driver_id)

    passenger_profile = PassengerProfile.objects.get(id=passenger_profile_id)

    review_content = request.POST.get('review_content')

    new_passenger_review = PassengerReview(driver=driver, passenger_profile=passenger_profile, review_content=review_content )

    new_passenger_review.save()

    data = {'success':'Your review has successfully been saved'}

    return JsonResponse(data)

# Passenger see drivers near them
@login_required(login_url='/new/passenger')
def driver_near_me(request, passenger_id):
    '''
    View function that displays a list of drivers near the general location of the current passenger
    '''
    passenger = Passenger.objects.get(id=passenger_id)

    passenger_profile = PassengerProfile.objects.get(passenger=passenger_id)

    title = f'Drivers near {passenger_profile.passenger.first_name} {passenger_profile.passenger.last_name}'

    passenger_general_location = passenger_profile.general_location

    travel_plans = TravelPlan.objects.all()

    close_drivers = TravelPlan.get_driver_near_me(passenger_general_location)

    if len(close_drivers) == 0:

        message = f'{passenger_general_location}'

        return render(request, 'all-passengers/driver-near-me.html', {"title":title, "message":message, "passenger":passenger})
    else:
        print(close_drivers)

        return render(request, 'all-passengers/driver-near-me.html', {"title":title, "close_drivers":close_drivers, "passenger": passenger})

    return print(len(close_drivers))





