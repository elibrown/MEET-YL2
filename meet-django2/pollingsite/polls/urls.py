from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	#ex. /polls/meet
	url(r^index/$,view.index , name="index"),
)
