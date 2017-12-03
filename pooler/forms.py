from django import forms
# from django.contrib.auth.forms import AuthenticationForm
from .models import Driver, DriverProfile, Passenger, PassengerProfile

class NewDriver(forms.ModelForm):
    '''
    Class to create a form for a user to sign up as a driver
    '''
    class Meta:
        model = Driver
        fields = ('first_name', 'last_name', 'phone_number')

class DriverLogin(forms.ModelForm):
    '''
    Class to create a form for a user to sign in as a driver
    '''
    class Meta:
        model = Driver
        fields = ('phone_number',)

class UpdateDriverProfile(forms.ModelForm):
    '''
    Class to create a form for a driver to change their profile
    '''
    class Meta:
        model = DriverProfile
        fields = ('gender', 'profile_pic', 'car_image', 'car_capacity', 'car_number_plate', 'car_color')

class NewPassenger(forms.ModelForm):
    '''
    Class to create a form for a user to sign up as a driver
    '''
    class Meta:
        model = Passenger
        fields = ('first_name', 'last_name', 'phone_number')

class PassengerLogin(forms.ModelForm):
    '''
    Class to create a form for a user to sign in as a passenger
    '''
    class Meta:
        model = Passenger
        fields = ('phone_number',)

class UpdatePassengerProfile(forms.ModelForm):
    '''
    Class to create a form for a passenger to change their profile
    '''
    class Meta:
        model = PassengerProfile
        fields = ('gender', 'profile_pic', 'general_location')


