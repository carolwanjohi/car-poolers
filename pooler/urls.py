from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url( r'^$', views.index, name="index"),

    url( r'^new/driver/', views.new_driver, name="newdriver"),

    url( r'^login/driver/', views.driver_login, name="driverlogin"),

    url( r'^driver/(\d+)', views.driver, name="driver"),

    url( r'^update/driver/profile/(\d+)', views.update_driver_profile, name="updateDriverProfile"),

    url( r'^new/passenger', views.new_passenger, name="newpassenger"),

    url( r'^passenger/(\d+)', views.passenger, name="passenger"),

    url( r'^login/passenger/', views.passenger_login, name="passengerlogin"),
    
    url( r'^update/passenger/profile/(\d+)', views.update_passenger_profile, name="updatePassengerProfile"),

    url( r'^drivers/(\d+)', views.drivers, name="drivers"),

    url( r'^profile/driver/(\d+)/(\d+)', views.driver_profile, name="driverProfile"),

    url( r'^ajax/review-driver/profile/driver/(\d+)/(\d+)', views.review_driver, name="reviewDriver"),

    url( r'^passengers/(\d+)', views.passengers, name="passengers"),

    url( r'^profile/passenger/(\d+)/(\d+)', views.passenger_profile, name="passengerProfile"),

    url( r'^ajax/review-passenger/profile/passenger/(\d+)/(\d+)', views.review_passenger, name="reviewPassenger"),

    url( r'^driver-near-me/(\d+)', views.driver_near_me, name="driverNearMe"),

    url( r'^new/journey/(\d+)', views.new_journey, name="newJourney"),

    url( r'^my-journies/(\d+)', views.current_journey, name="currentJourney")

]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )