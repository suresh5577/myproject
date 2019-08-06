from django.urls import path, re_path
from service.views import LeaveAPI
urlpatterns = [
	re_path("leaves/$",LeaveAPI.as_view()),
	re_path("leaves/(?P<pk>[0-9]+)",LeaveAPI.as_view())
]