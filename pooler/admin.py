from django.contrib import admin
from .models import Driver, DriverProfile

# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     '''
#     Customise model in admin page
#     '''
#     filter_horizontal = ('tags',)

admin.site.register(Driver)
admin.site.register(DriverProfile)
# admin.site.register(Post,PostAdmin)
# admin.site.register(Follow)
# admin.site.register(Comment)
# admin.site.register(Like)