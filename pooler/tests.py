from django.test import TestCase
from .models import Driver

# Create your tests here.
class DriverTestClass(TestCase):
    '''
    Test case for the Driver class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Driver class
        '''
        # Create instance of D class
        self.new_driver = Driver(first_name="James",last_name="Muriuki",phone_number=0712345656)

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