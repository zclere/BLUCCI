from django.contrib import admin
from .models import *



class FeaturedContentAdmin(admin.ModelAdmin):

	def get_exclude(self, request, obj=None):
		excluded = super().get_exclude(request, obj) or [] # get overall excluded fields

		if not request.user.is_superuser: # if user is not a superuser
			return excluded + ['user']

		return excluded # otherwise return the default excluded fields if any

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)


	def has_add_permission(self, request):
		num_objects = self.model.objects.filter(user=request.user).count()
		if num_objects >= 3:
			return False
		else:
			return True


	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'featured_content':
			kwargs["queryset"] = ContentList.objects.filter(
				user=request.user
				)
		return super(FeaturedContentAdmin, self).formfield_for_foreignkey(
			db_field, request, **kwargs
			)



	def get_queryset(self, request):
		qs = super().get_queryset(request)
		user = request.user
		return qs if user.is_superuser else qs.filter(user=user)


admin.site.register(FeaturedContent, FeaturedContentAdmin)