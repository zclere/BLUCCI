from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	birthday = models.DateField(null=True, blank=True)
	gender = models.CharField(max_length=15, choices=GENDER_CHOICES)


	def __str__(self):
		return self.user.username


