
from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from . import views

app_name = 'guest'

urlpatterns = [
	url(r'^(?P<pk>\d+)/$', views.ProfileView.as_view() ,name='profile'),
	url(r'^update/$', login_required(views.ProfileUpdateView.as_view()),name='profile-update'),

	#url(r'^update/$', login_required(views.ProfileUpdateView.as_view()),name='profile-update'),
	#url(r'^all/$', login_required(views.users_view),name='all'),

]