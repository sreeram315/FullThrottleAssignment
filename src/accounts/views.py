from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, exceptions, response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from django.contrib.auth.models import User
from .models import ActivityPeriod



class ActivityPeriodAPIView(APIView):
	permission_classes = (
		permissions.AllowAny,
		)

	def get_user_data(self, user):
		activity_periods = ActivityPeriod.objects.filter(user = user)
		activity_periods = [{"start_time": t.start_time, "end_time": t.end_time} for t in activity_periods]
		user_data = {
				"ID": 				user.userprofile.identity_number,
				"real_name":		user.userprofile.real_name,
				"tz": 				user.userprofile.timezone,
				"activity_periods": activity_periods
		}
		return user_data

	def get(self, request):
		users 		= 	User.objects.all()
		members 	=	[]
		for user in users:
			members.append(self.get_user_data(user))
		response_text = {
						"ok": True,
						"members": members
				}
		return response.Response(response_text)


