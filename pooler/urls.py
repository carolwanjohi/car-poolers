from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url( r'^$', views.index, name="index"),
    url( r'^new/driver/', views.new_driver, name="newdriver"),
    url( r'^login/driver/', views.driver_login, name="driverlogin"),
    url( r'driver/(\d+)', views.driver, name="driver"),
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )