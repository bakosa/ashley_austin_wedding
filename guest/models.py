from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db import transaction, IntegrityError
import os
from stdimage.models import StdImageField

# Create your models here.

class Code(models.Model):
	code = models.CharField(blank=False,null=-False,max_length=10)
	used_already = models.BooleanField(default=False)
	can_add_plus_one = models.BooleanField(default=False)



######################################################################################
############################### User Profile #########################################

def get_image_path(instance, filename):
	return os.path.join("guest",str(instance.user.username),filename)

class UserFullName(User):
	class Meta:
		proxy = True
	def __unicode__(self):
		return self.get_full_name() 

User._meta.ordering = ['last_name', 'first_name']

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_image = StdImageField( blank=True,null=-True, variations={
		'large': (600, 400),
		'thumbnail': (168, 168, True),
		'medium': (300, 200),
	})
	invitation_code = models.CharField(blank=True,null=-True,max_length=10)

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('guest:profile', kwargs={ 'pk':self.user.pk })
	def __str__(self):
		return self.user.first_name + ' ' + self.user.last_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		try:
			newProfile = Profile.objects.create(user=instance)
			newProfile.save()
		except:
			pass

@receiver(post_save, sender=User) 
def save_user_profile(sender, instance, **kwargs):
    user = instance
    try:
        with transaction.atomic():
            user.profile.save()
    except IntegrityError:
        profile = Profile.objects.create(user=instance)
        profile.save()
