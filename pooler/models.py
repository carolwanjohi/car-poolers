from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

# Gender options for the gender field in profile forms
Gender_Choices = (
    ('F', 'female'),
    ('M', 'male'),
    ('Both', 'both'),
    ('None', 'non-specified'),
)

# Alphanumeric generator
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

DEFAULTCAR = "car-image/car-default.png"

DEFAULTDRIVERPROFILEPIC = "driver/profile-pic/user-icon.png"

DEFAULTPASSANGERPROFILEPIC = "passenger/profile-pic/user-icon.png"

# Create your models here.
class Driver(models.Model):
    '''
    Class that defines a Driver in the application
    '''
    first_name = models.CharField(max_length=180)

    last_name = models.CharField(max_length=180)

    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name  + ' ' + self.last_name

    @classmethod
    def get_drivers(cls):
        '''
        Function that gets all the drivers in the database
        '''
        drivers = Driver.objects.all()

        return drivers

class DriverProfile(models.Model):
    '''
    Class that defines a profile for a Driver
    '''
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)

    profile_pic = models.ImageField(blank=True,upload_to="driver/profile-pic", default=DEFAULTDRIVERPROFILEPIC)

    car_image = models.ImageField(blank=True,upload_to="car-image/", default=DEFAULTCAR)

    car_capacity = models.PositiveIntegerField(default=0, blank=True)

    car_number_plate = models.CharField(blank=True, max_length=60, validators=[alphanumeric])

    car_color = models.CharField(max_length=255, blank=True)

    gender = models.CharField(
        max_length=30, choices=Gender_Choices, default='None', blank=True)

    def __str__(self):
        return self.driver.first_name + ' ' + self.driver.last_name

    @classmethod
    def get_driver_profiles(cls):
        '''
        Function that gets all the driver profiles in the database
        '''
        driver_profiles = DriverProfile.objects.all()

        return driver_profiles

# Create Driver Profile when creating a Driver
@receiver(post_save, sender=Driver)
def create_driverprofile(sender, instance, created, **kwargs):
    if created:
        DriverProfile.objects.create(driver=instance)

# Save Driver Profile when saving a Driver
@receiver(post_save, sender=Driver)
def save_driverprofile(sender, instance, **kwargs):
    instance.driverprofile.save()

class Passenger(models.Model):
    '''
    Class that defines a Passenger in the application
    '''
    first_name = models.CharField(max_length=180)

    last_name = models.CharField(max_length=180)

    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name  + ' ' + self.last_name

    @classmethod
    def get_passengers(cls):
        '''
        Function that gets all the passengers in the database
        '''
        passengers = Passenger.objects.all()

        return passengers

class PassengerProfile(models.Model):
    '''
    Class that defines a profile for a Passenger
    '''
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

    profile_pic = models.ImageField(blank=True, upload_to="passenger/profile-pic", default=DEFAULTPASSANGERPROFILEPIC)

    gender = models.CharField(
        max_length=30, choices=Gender_Choices, default='None', blank=True)

    general_location = models.CharField(blank=True,max_length=255)

    def __str__(self):
        return self.passenger.first_name + ' ' + self.passenger.last_name

    @classmethod
    def get_passenger_profiles(cls):
        '''
        Function that gets all the passenger profiles in the database
        '''
        passenger_profiles = PassengerProfile.objects.all()

        return passenger_profiles

# Create Passenger Profile when creating a Passenger
@receiver(post_save, sender=Passenger)
def create_passengerprofile(sender, instance, created, **kwargs):
    if created:
        PassengerProfile.objects.create(passenger=instance)

# Save Passenger Profile when saving a Passenger
@receiver(post_save, sender=Passenger)
def save_passengerprofile(sender, instance, **kwargs):
    instance.passengerprofile.save()

class DriverReview(models.Model):
    '''
    Class that defines the reviews a passenger gives a driver
    '''
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    driver_profile = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)

    review_content = models.TextField()

    def __str__(self):
        return self.passenger.first_name + ' ' + self.passenger.last_name

    @classmethod
    def get_driver_reviews(self,driver_profile_id):
        '''
        Function that gets all the reviews a specific driver's profile gets from passengers

        Args:
            driver_profile_id : specific driver profile id

        Returns:
            driver_reviews : Driver Review objects belonging to a specific driver profile
        '''
        driver_reviews = DriverReview.objects.filter(driver_profile=driver_profile_id)

        return driver_reviews

class PassengerReview(models.Model):
    '''
    Class that defines the reviews a driver gives a passenger
    '''
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    passenger_profile = models.ForeignKey(PassengerProfile, on_delete=models.CASCADE)

    review_content = models.TextField()

    def __str__(self):
        return self.driver.first_name + ' ' + self.driver.last_name

    @classmethod
    def get_passenger_reviews(self,passenger_profile_id):
        '''
        Function that gets all the reviews a specific passenger's profile gets from drivers

        Args:
            passenger_profile_id : specific passenger profile id

        Returns:
            passenger_reviews : Passenger Review objects belonging to a specific passenger profile
        '''
        passenger_reviews = PassengerReview.objects.filter(passenger_profile=passenger_profile_id)

        return passenger_reviews

class TravelPlan(models.Model):
    '''
    Class that defines the current location and the destination of the driver
    '''
    driver_profile = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)

    current_location = models.CharField(max_length=255)

    destination = models.CharField(max_length=255)

    travel_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        '''
        Order travel plans with most recent at the top
        '''
        ordering = ['-travel_date']

    def __str__(self):
        return self.driver_profile.driver.first_name + ' ' + self.driver_profile.driver.last_name

    @classmethod
    def get_driver_near_me(cls,passenger_general_location):
        '''
        Function that gets Travel Plan objects that have a current location matching the general location of a passenger

        Args:
            passenger_general_location : the general_location of a passenger

        Returns:
            close_drivers : list of Travel Plan objects with current location that match the passenger general location
        '''
        close_drivers = TravelPlan.objects.filter(current_location__icontains=passenger_general_location)

        return close_drivers












