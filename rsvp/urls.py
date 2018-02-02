
from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from . import views

app_name = 'rsvp'

urlpatterns = [
	url(r'^submit/$', login_required(views.rsvp_view),name='rsvp'),
	url(r'^success/$', login_required( views.rsvp_success_view),name='success'),

	#url(r'^update/$', login_required(views.ProfileUpdateView.as_view()),name='profile-update'),
	#url(r'^all/$', login_required(views.users_view),name='all'),

]