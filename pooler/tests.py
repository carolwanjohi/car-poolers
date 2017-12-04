from django.test import TestCase
from .models import Driver, DriverProfile, Passenger, PassengerProfile, DriverReview, PassengerReview, TravelPlan

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
        Method that creates an instance of Driver Profile class
        '''
        # Create instance of Drive Profile class
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

class PassengerProfileTestClass(TestCase):
    '''
    Test case for the Passenger Profile class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Passenger Profile class
        '''
        # Create instance of Passenger Profile class
        self.new_passenger_profile = PassengerProfile(general_location="Nairobi")

    def test_instance(self):
        '''
        Test case to check if self.new_passenger_profile in an instance of Passenger class
        '''
        self.assertTrue( isinstance(self.new_passenger_profile, PassengerProfile) )

    def test_get_get_passenger_profiles(self):
        '''
        Test case to check if all passenger profiles are gotten from the database
        '''
        gotten_passenger_profiles = PassengerProfile.get_passenger_profiles()

        passenger_profiles = PassengerProfile.objects.all()

        self.assertTrue( len(gotten_passenger_profiles) == len(passenger_profiles))

class DriverReviewTestClass(TestCase):
    '''
    Test case for the Driver Review class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Driver Review class
        '''
        # Create a Driver Review instance
        self.new_driver_review = DriverReview(review_content ='Python James is Muriuki who wrote Python content for Moringa School')

    def test_instance(self):
        '''
        Test case to check if self.new_driver_review in an instance of Driver Review class
        '''
        self.assertTrue( isinstance(self.new_driver_review, DriverReview) )

    def test_get_driver_reviews(self):
        '''
        Test case to check if get driver reviews is getting driver reviews for a specific driver profile
        '''
        self.james = Driver(first_name="James", last_name="Muriuki", phone_number="0712345656")
        self.james.save()

        self.jane = Passenger(first_name="Jane", last_name="Doe", phone_number="0712987987")
        self.jane.save()

        self.test_driver_profile = DriverProfile(driver=self.james, car_capacity=4, car_number_plate="MSA234", car_color="blue")

        self.test_driver_review = DriverReview(passenger=self.jane, driver_profile=self.test_driver_profile,review_content="Wow")

        gotten_driver_reviews = DriverReview.get_driver_reviews(self.test_driver_profile.id)

        driver_reviews = DriverReview.objects.all()

        # No driver reviews were saved so expect True
        self.assertTrue( len(gotten_driver_reviews) == len(driver_reviews))

class PassengerReviewTestClass(TestCase):
    '''
    Test case for the Passenger Review class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Passenger Review class
        '''
        # Create a Passenger Review instance
        self.new_passenger_review = PassengerReview(review_content ='Python James is Muriuki who wrote Python content for Moringa School')

    def test_instance(self):
        '''
        Test case to check if self.new_passenger_review in an instance of Passenger Review class
        '''
        self.assertTrue( isinstance(self.new_passenger_review, PassengerReview) )

    def test_get_passenger_reviews(self):
        '''
        Test case to check if get passenger reviews is getting passenger reviews for a specific passenger profile
        '''
        self.james = Driver(first_name="James", last_name="Muriuki", phone_number="0712345656")
        self.james.save()

        self.jane = Passenger(first_name="Jane", last_name="Doe", phone_number="0712987987")
        self.jane.save()

        self.test_passenger_profile = PassengerProfile(passenger=self.jane, general_location="Nairobi")

        self.test_passenger_review = PassengerReview(driver=self.james, passenger_profile=self.test_passenger_profile,review_content="Wow")

        gotten_passenger_reviews = PassengerReview.get_passenger_reviews(self.test_passenger_profile.id)

        passenger_reviews = PassengerReview.objects.all()

        # No passenger reviews were saved so expect True
        self.assertTrue( len(gotten_passenger_reviews) == len(passenger_reviews))


class TravelPlanTestClass(TestCase):
    '''
    Test case for Travel Plan class
    '''

    # Set Up method
    def setUp(self):
        '''
        Method that sets up a Travel Plan instance before each test
        '''
        # Create a Travel Plan instance
        self.new_travel_plan = TravelPlan(current_location='Karen', destination='Thika')

    def test_instance(self):
        '''
        Test case to check if self.new_travel_plan is an instance of TravelPlan class
        '''
        self.assertTrue( isinstance(self.new_travel_plan, TravelPlan) )

    def test_get_driver_near_me(self):
        '''
        Test case to check if get driver near me gets Travel Plan objects that contain the general location of a passenger
        '''
        self.james = Driver(first_name="James", last_name="Muriuki", phone_number="0712345656")
        self.james.save()

        self.jane = Passenger(first_name="Jane", last_name="Doe", phone_number="0712987987")
        self.jane.save()

        self.test_driver_profile = DriverProfile(driver=self.james, car_capacity=4, car_number_plate="MSA234", car_color="blue")

        self.test_passenger_profile = PassengerProfile(passenger=self.jane, general_location="Kasarani")

        self.test_travel_plan = TravelPlan(driver_profile=self.test_driver_profile ,current_location='Kasarani', destination='Karen')

        gotten_close_drivers = TravelPlan.get_driver_near_me(self.test_passenger_profile.general_location)

        travel_plans = TravelPlan.objects.all()

        # No travel plans were saved so expect True
        self.assertTrue( len(gotten_close_drivers) == len(travel_plans))


