from django.forms import ModelForm
from .models import Profile, Code
from django import forms
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['invitation_code']

	def clean_invitation_code(self):
		code = self.cleaned_data['invitation_code']
		if not Code.objects.filter(code=code.upper()).exists():
			raise forms.ValidationError("Invalid Code!")
		#else: 
		#	code = Code.objects.get(code=self.cleaned_data['invitation_code'])
			#if code.used_already:
			#	raise forms.ValidationError("Code Has Already Been Used!")
		#	else:
		#		code.used_already = True; 
		#		code.save() 
		# Always return a value to use as the new cleaned data, even if
		# this method didn't change it.
		return code.upper()


#validate code