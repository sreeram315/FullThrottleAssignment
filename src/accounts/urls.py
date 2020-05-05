from django.conf.urls import url
from django.views.generic import TemplateView

from .views import ActivityPeriodAPIView


urlpatterns = [
	url(r'activity-period/$', ActivityPeriodAPIView.as_view(), name = 'activity-period'),
	

]

