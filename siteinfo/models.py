from django.db import models
import datetime
# Create your models here.


class PrivacyPolicy(models.Model):
	policy = models.TextField()

	def __str__(self):
		return "Privacy Policy"

	class Meta:
	    verbose_name = "Privacy Policy"
	    verbose_name_plural = "Privacy Policy"



class TermsPolicy(models.Model):
	policy = models.TextField()

	def __str__(self):
		return "Terms & Conditions"

	class Meta:
	    verbose_name = "Terms & Conditions"
	    verbose_name_plural = "Terms & Conditions"

