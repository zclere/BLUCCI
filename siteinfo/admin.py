from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE


class PrivacyPolicyAdmin(admin.ModelAdmin):


	def has_add_permission(self, request):
		num_objects = self.model.objects.count()
		if num_objects >= 1:
			return False
		else:
			return True

	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


class TermsPolicyAdmin(admin.ModelAdmin):


	def has_add_permission(self, request):
		num_objects = self.model.objects.count()
		if num_objects >= 1:
			return False
		else:
			return True

	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }



admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)


admin.site.register(TermsPolicy, TermsPolicyAdmin)