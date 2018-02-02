from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Response(models.Model):
	guest = models.ForeignKey(User, related_name="response", null=False, blank=False, on_delete=models.CASCADE)
	ATTENDING_CHOICES = (
		('Y','Yes'),
		('N','No'),
	)
	attending = models.CharField(max_length=1, null=False, blank=False, choices=ATTENDING_CHOICES, default='Y')
	comments = models.CharField(max_length=255, blank=True, null=True )
	response_date = models.DateTimeField(blank=False, null=False, auto_now_add=True)
	plus_one = models.CharField(max_length=1, null=True, blank=True, choices=ATTENDING_CHOICES, default=None)

	class Meta:
		permissions = (
			("can_add_plus_one", "Need this permission to add a plus one"),
		)

#def get_absolute_url(self):
#		return reverse('mountains:mountain', kwargs={ 'pk':self.pk })
