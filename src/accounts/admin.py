from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.UserProfile)
class AccountAdmin(admin.ModelAdmin):
    fields          =   (  "user", "identity_number", "real_name", "contact_number", "timezone", "email")
    list_display    = 	fields + ( "created_on", "updated_on" )

    list_display_links  = list_display
    model           =   models.UserProfile
    extra           =   0


@admin.register(models.ActivityPeriod)
class ActivityPeriodAdmin(admin.ModelAdmin):
    fields          =   (  "user", "start_time", "end_time")
    list_display    = 	fields + ( "created_on", "updated_on" )

    list_display_links  = list_display
    model           =   models.ActivityPeriod
    extra           =   0