from django.db import models

# Create your models here.
class Driver(models.Model):
    '''
    Class that defines a Driver in the application
    '''
    first_name = models.CharField(max_length=180)

    last_name = models.CharField(max_length=180)

    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name + self.last_name

    @classmethod
    def get_drivers(cls):
        '''
        Function that gets all the drivers in the database
        '''
        drivers = Driver.objects.all()

        return drivers


