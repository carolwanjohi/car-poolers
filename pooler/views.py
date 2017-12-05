from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Driver, DriverProfile, Passenger, PassengerProfile, DriverReview, PassengerReview, TravelPlan
from .forms import NewDriver, DriverLogin, UpdateDriverProfile, NewPassenger, PassengerLogin, UpdatePassengerProfile, ReviewDriverForm, ReviewPassengerForm, NewTravelPlan
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

            drivers = Driver.objects.all()

            for existing_driver in drivers:

                if new_driver.phone_number != existing_driver.phone_number:
                    message = 'The number is already registered'

                    messages.error(request, ('This number is already registered'))

                    return render(request, 'registration/driver/registration_form.html', {"title":title, "form":form, "message":message})

                else:
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

    try:

        if request.method == 'POST':

            form = DriverLogin(request.POST)

            if form.is_valid:

                phone_number = request.POST.get('phone_number')

                try:
                    found_driver = Driver.objects.get(phone_number=phone_number)

                    print(found_driver)

                    return redirect(driver, found_driver.id)

                except ObjectDoesNotExist:
                    raise Http404()

            else:

                messages.error(request, ('Please correct the error below.'))

        else:
            form = DriverLogin()

            return render(request, 'registration/driver/login.html',{"title":title,"form":form})

    except ObjectDoesNotExist:
        raise Http404()

# Drive homepage is Profile page
def driver(request, id):
    '''
    View function to display an authenticated logged in driver's profile
    '''
    drivers = Driver.objects.all()

    try:

        driver = Driver.objects.get(id=id)

        if driver in drivers:

            title = f'{driver.first_name} {driver.last_name}'

            driver_profile = DriverProfile.objects.get(driver=driver)

            return render(request, 'all-drivers/profile.html', {"title":title, "driver":driver, "driver_profile":driver_profile})

        else:
            return redirect(driver_login)

    except ObjectDoesNotExist:
        raise Http404()

# Driver update profile
@transaction.atomic
def update_driver_profile(request, id):
    '''
    View function to display an update driver profile form for an authenticated driver
    '''
    drivers = Driver.objects.all()

    try:

        found_driver = Driver.objects.get(id=id)

        if found_driver in drivers:

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

        else:

            return redirect(driver_login)

    except ObjectDoesNotExist:
        raise Http404()

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

            passengers = Passenger.objects.all()

            for existing_passenger in passengers:

                if new_passenger.phone_number != existing_passenger.phone_number:
                    message = 'The number is already registered'

                    messages.error(request, ('This number is already registered'))

                    return render(request, 'registration/passenger/registration_form.html', {"title":title, "form":form, "message":message})

                else:
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
def passenger(request, id):
    '''
    View function to display an authenticated logged in passenger's profile
    '''
    passengers = Passenger.objects.all()

    try:

        passenger = Passenger.objects.get(id=id)

        if passenger in passengers :

            title = f'{passenger.first_name} {passenger.last_name}'

            passenger_profile = PassengerProfile.objects.get(passenger=passenger)

            return render(request, 'all-passengers/profile.html', {"title":title, "passenger":passenger, "passenger_profile":passenger_profile})

        else :
            return redirect(passenger_login)

    except ObjectDoesNotExist:
        raise Http404()


# Passenger update profile 
@transaction.atomic
def update_passenger_profile(request, id):
    '''
    View function to display an update passenger profile form for an authenticated passenger
    '''
    passengers = Passenger.objects.all()

    try:

        found_passenger = Passenger.objects.get(id=id)

        if found_passenger in passengers:

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

        else:
            return redirect(passenger_login)

    except ObjectDoesNotExist:
        raise Http404()


# Passenger see list of drivers
def drivers(request,id):
    '''
    View function to display list of driver profiles
    '''
    passengers = Passenger.objects.all()

    try:

        passenger = Passenger.objects.get(id=id)

        if passenger in passengers:

            title = "Driver Reviews"

            driver_profiles = DriverProfile.objects.all()

            return render(request, "all-passengers/reviews.html", {"title":title,"passenger":passenger, "driver_profiles":driver_profiles})
        else:

            return redirect(passenger_login)

    except ObjectDoesNotExist:
        raise Http404()

# Passenger see selected driver's profile and reviews
def driver_profile(request, passenger_id, driver_profile_id):
    '''
    View function to display list of driver profiles
    '''
    passengers = Passenger.objects.all()

    try:

        passenger = Passenger.objects.get(id=passenger_id)

        if passenger in passengers:

            driver_profile = DriverProfile.objects.get(id=driver_profile_id)

            title = f'{driver_profile.driver.first_name} {driver_profile.driver.last_name}\'s Profile'

            reviews = DriverReview.get_driver_reviews(driver_profile_id)

            form = ReviewDriverForm()

            return render(request, "all-passengers/driver-profile.html", {"title":title, "passenger":passenger, "driver_profile":driver_profile, "reviews":reviews, "form":form})

        else:

            return redirect(passenger_login)

    except ObjectDoesNotExist:
        raise Http404()


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

# Driver sees list of passengers
def passengers(request,id):
    '''
    View function to display list of passenger profiles
    '''
    drivers = Driver.objects.all()

    try:

        driver = Driver.objects.get(id=id)

        if driver in drivers:

            title = "Passenger Reviews"

            passenger_profiles = PassengerProfile.objects.all()

            return render(request, "all-drivers/reviews.html", {"title":title,"driver":driver, "passenger_profiles":passenger_profiles})
        else:

            return redirect(driver_login)

    except ObjectDoesNotExist:
        raise Http404()


# Driver see selected passenger's profile and reviews
@login_required(login_url='/login/driver')
def passenger_profile(request, driver_id, passenger_profile_id):
    '''
    View function to display list of driver profiles
    '''
    drivers = Driver.objects.all()

    try:

        driver = Driver.objects.get(id=driver_id)

        if driver in drivers:

            passenger_profile = PassengerProfile.objects.get(id=passenger_profile_id)

            title = f'{passenger_profile.passenger.first_name} {passenger_profile.passenger.last_name}\'s Profile'

            reviews = PassengerReview.get_passenger_reviews(passenger_profile_id)

            form = ReviewPassengerForm()

            return render(request, "all-drivers/passenger-profile.html", {"title":title, "driver":driver, "passenger_profile":passenger_profile, "reviews":reviews, "form":form})

        else:

            return redirect(driver_login)

    except ObjectDoesNotExist:
        raise Http404()


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
def driver_near_me(request, passenger_id):
    '''
    View function that displays a list of drivers near the general location of the current passenger
    '''
    passengers = Passenger.objects.all()

    try:

        passenger = Passenger.objects.get(id=passenger_id)

        if passenger in passengers:

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

        else:

            return redirect(passenger_login)

    except ObjectDoesNotExist:
        raise Http404()


# Driver begins a new journey
def new_journey(request, driver_profile_id):
    '''
    View function to display a form for creating a new travel plan 
    '''
    title = "New Journey"

    try:

        driver_profile = DriverProfile.objects.get(id=driver_profile_id)

        found_driver = driver_profile.driver

        drivers = Driver.objects.all()

        if found_driver in drivers:

            if request.method == 'POST':

                form = NewTravelPlan(request.POST)

                if form.is_valid:

                    new_travel_plan = form.save(commit=False)

                    new_travel_plan.driver_profile = driver_profile

                    new_travel_plan.save()

                    return redirect(current_journey, found_driver.id)

                else :

                    messages.error(request, ('Please correct the error below.'))

            else : 

                form = NewTravelPlan()

                return render(request, 'all-drivers/new-journey.html', {"title": title, "form": form, "driver":found_driver})

        else:

            return redirect(driver_login)

    except ObjectDoesNotExist:
        raise Http404()


# Display list of journeys the current driver has
def current_journey(request,driver_id):
    '''
    View function to display a driver's travel plans
    '''
    drivers = Driver.objects.all()

    try:

        driver = Driver.objects.get(id=driver_id)

        if driver in drivers:

            driver_profile = driver.driverprofile

            travel_plans = TravelPlan.objects.filter(driver_profile=driver_profile)

            title = f'{driver.first_name} {driver.last_name}\'s Journeys'

            return render(request, 'all-drivers/current_journey.html', {"title":title, "driver":driver, "travel_plans":travel_plans, "driver_profile":driver_profile})

        else:

            return redirect(driver_login)

    except ObjectDoesNotExist:
        raise Http404()







