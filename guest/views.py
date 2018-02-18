from django.shortcuts import render
from django.views import generic
from .models import Profile, Code
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from .forms import ProfileForm
from django.contrib.auth.models import Permission
# Create your views here.
class ProfileView(generic.DetailView):
	model = User
	template_name = 'guest/profile.html'

class ProfileUpdateView(UpdateView):
	model = Profile
	form_class = ProfileForm
	template_name_suffix = '_update_form'
	def form_valid(self, form):
		# Allows guest to RSVP 
		self.request.user.user_permissions.add(Permission.objects.get(codename='add_response'))
		self.request.user.user_permissions.add(Permission.objects.get(codename='change_response'))
		# Allows guest to vote on Keg code here#
		
		# Check if they can have plus one 
		code = Code.objects.get(code=form.cleaned_data['invitation_code'])
		if code.can_add_plus_one:
			self.request.user.user_permissions.add(Permission.objects.get(codename='can_add_plus_one'))

		return super(ProfileUpdateView, self).form_valid(form)

	def get_object(self, queryset=None):
		return self.request.user.profile



class Guests_View(generic.ListView):
	model = User
	context_object_name = 'users'
	template_name = 'guest/guests.html'
	def get_queryset(self):
		return User.objects.all().order_by('last_name')