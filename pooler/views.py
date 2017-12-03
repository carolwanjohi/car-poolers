from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Driver, DriverProfile
from .forms import NewDriver, NewDriverProfile
from django.contrib import messages
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
    title = 'Welcome Driver'

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


@login_required(login_url='/new/driver/')
def driver(request, id):
    '''
    View function to display an authenticated logged in driver's profile
    '''
    # current_user = request.driver

    # print(current_user)

    driver = Driver.objects.get(id=id)

    title = f'{driver.first_name}'

    message = f'{driver.first_name} {driver.last_name}\'s Profile'

    return render(request, 'all-drivers/profile.html', {"title":title,"message":message, "driver":driver})






