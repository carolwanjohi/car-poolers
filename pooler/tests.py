from django.test import TestCase
from .models import Driver, DriverProfile, Passenger

# Create your tests here.
class DriverTestClass(TestCase):
    '''
    Test case for the Driver class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Driver class
        '''
        # Create instance of Driver class
        self.new_driver = Driver(first_name="James",last_name="Muriuki",phone_number="0712345656")

    def test_instance(self):
        '''
        Test case to check if self.new_driver in an instance of Driver class
        '''
        self.assertTrue( isinstance(self.new_driver, Driver) )

    def test_get_drivers(self):
        '''
        Test case to check if all drivers are gotten from the database
        '''
        gotten_drivers = Driver.get_drivers()

        drivers = Driver.objects.all()

        self.assertTrue( len(gotten_drivers) == len(drivers))

class DriverProfileTestClass(TestCase):
    '''
    Test case for the Driver Profile class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Driver class
        '''
        # Create instance of D class
        self.new_driver_profile = DriverProfile(car_capacity=4, car_number_plate="MSA234", car_color="blue")

    def test_instance(self):
        '''
        Test case to check if self.new_driver_profile in an instance of Driver class
        '''
        self.assertTrue( isinstance(self.new_driver_profile, DriverProfile) )

    def test_get_driver_profiles(self):
        '''
        Test case to check if all driver profiles are gotten from the database
        '''
        gotten_driver_profiles = DriverProfile.get_driver_profiles()

        driver_profiles = DriverProfile.objects.all()

        self.assertTrue( len(gotten_driver_profiles) == len(driver_profiles))

class PassengerTestClass(TestCase):
    '''
    Test case for the Passenger class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Passenger class
        '''
        # Create instance of Passenger class
        self.new_passenger = Passenger(first_name="James",last_name="Muriuki",phone_number="0712345656")

    def test_instance(self):
        '''
        Test case to check if self.new_passenger in an instance of Passenger class
        '''
        self.assertTrue( isinstance(self.new_passenger, Passenger) )

    def test_get_passengers(self):
        '''
        Test case to check if all passengers are gotten from the database
        '''
        gotten_passengers = Passenger.get_passengers()

        passengers = Passenger.objects.all()

        self.assertTrue( len(gotten_passengers) == len(passengers))


