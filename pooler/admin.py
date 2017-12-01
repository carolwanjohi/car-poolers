from django.contrib import admin
from .models import Driver, DriverProfile, Passenger, PassengerProfile

# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     '''
#     Customise model in admin page
#     '''
#     filter_horizontal = ('tags',)

admin.site.register(Driver)
admin.site.register(DriverProfile)
admin.site.register(Passenger)
admin.site.register(PassengerProfile)
# admin.site.register(Post,PostAdmin)
# admin.site.register(Comment)
# admin.site.register(Like)