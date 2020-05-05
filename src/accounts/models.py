from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class UserProfile(models.Model):
    user                    = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'userprofile')
    identity_number		 	= models.CharField(max_length = 127, blank=True, null=True)
    real_name 				= models.CharField(max_length = 127, blank=True, null=True)
    timezone 				= models.CharField(max_length = 127, blank=True, null=True)
    contact_number 			= models.CharField(max_length = 12, blank=True, null=True)
    email 					= models.CharField(max_length = 120, blank=True, null=True)

    created_on              = models.DateTimeField(auto_now_add=True, null = True, blank  =True)
    updated_on 			    = models.DateTimeField(auto_now=True, null = True, blank  =True)


    class Meta:
        db_table            = "tbl_userprofile"
        verbose_name        = "UserProfile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return f'{self.user.id} - {self.user.username}'



class ActivityPeriod(models.Model):
	user 					= models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'activity_period')
	start_time				= models.DateTimeField(blank = True, null = True)
	end_time 				= models.DateTimeField(blank = True, null = True)

	created_on              = models.DateTimeField(auto_now_add=True, null = True, blank  =True)
	updated_on 			    = models.DateTimeField(auto_now=True, null = True, blank  =True)



	class Meta:
		db_table            = "tbl_activity_period"
		verbose_name        = "Activity Period"
		verbose_name_plural = "User Activity Periods"

	def __str__(self):
		return f'{self.user.username} - {self.user.username}'



