from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from . import views

app_name = 'home'

urlpatterns = [
	url(r'^(?P<pk>\d+)/$', login_required(views.Mountain_Detail_View.as_view()),name='mountain'),
	url(r'^condition/(?P<pk>\d+)/$', login_required(views.mountian_conditions_ajax_view),name='condition-ajax'),
	url(r'^update/(?P<pk>\d+)/$', login_required(views.Mountain_Update_View.as_view()),name='mountain-update'),
	url(r'^add-or-remove-my-mountains/(?P<mountain_pk>\d+)/$', login_required(views.add_remove_mountain_to_my_mountains_view),name='add-remove-to-my-mountains'),
	url(r'^create/$', login_required(views.Mountain_Create_View.as_view()),name='mountain-create'),
	url(r'^$', login_required(views.Mountains_View.as_view()),name='mountains'),
]