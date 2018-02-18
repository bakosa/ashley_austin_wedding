from django.shortcuts import render
from .models import Response
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic
from .forms import RSVP_Form
from django.contrib.auth.models import User
# Create your views here.


def rsvp_success_view(request):
	return render(request,'rsvp/success.html', {})



def rsvp_view(request):
	if request.user.has_perm('rsvp.add_response'):
		return Response_Create_View.as_view()(request)
	else:
		return render(request,'rsvp/access_denied.html')		


class Response_Create_View(generic.CreateView):
	model = Response
	template_name = 'rsvp/rsvp.html'
	form_class = RSVP_Form
	success_url = reverse_lazy('rsvp:success')
	def form_valid(self, form):
		form.instance.guest = self.request.user 
		if self.request.user.response.first() is not None:
			form.add_error('attending', str(self.request.user.first_name) + ', you have alreay sent your RSVP!') 
			return super(Response_Create_View,self).form_invalid(form)
		else:
			if not self.request.user.profile.invitation_code:
				form.add_error('attending', str(self.request.user.first_name) + ', you dont have access to RSVP. Make sure to enter your invitation code in your profile') 
				return super(Response_Create_View,self).form_invalid(form)
			if form.cleaned_data['plus_one'] and not self.request.user.has_perm('rsvp.can_add_plus_one'):
				form.add_error('attending', str(self.request.user.first_name) + ', Really?... you dont have permission to add a plus 1.') 
				return super(Response_Create_View,self).form_invalid(form)
			response = super(Response_Create_View,self).form_valid(form)
			self.object.guest = self.request.user
			self.object.save()
			return response











