from django.forms import ModelForm
from .models import Response
from django import forms
from django.contrib.auth.models import User



class RSVP_Form(ModelForm):

	class Meta:
		model = Response
		fields = ['attending','plus_one', 'comments']
		widgets = {
			'comments': forms.Textarea(attrs={'rows':4, 'cols':15}),
		}
