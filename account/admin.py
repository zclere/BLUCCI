from django.contrib import admin
from .models import *


# Register your models here.


class ProfileAdmin(admin.StackedInline):
	model = Profile
	extra = 0

class UserAdmin(admin.ModelAdmin):
	inlines = [ProfileAdmin]

	readonly_fields = ["last_login", 'date_joined']


	def get_queryset(self, request):
		qs = super().get_queryset(request)
		user = request.user
		return qs if user.is_superuser else qs.filter(id=user.id)



	def get_exclude(self, request, obj=None):
		excluded = super().get_exclude(request, obj) or [] # get overall excluded fields

		if not request.user.is_superuser: # if user is not a superuser
			return excluded + ['password', 'groups', 'is_superuser', 'is_staff', 'user_permissions', 'is_active']

		return excluded # otherwise return the default excluded fields if any



	def has_change_permission(self, request, obj=None):
		if not obj is None and obj.id == 6:
			return False
		return request.user.is_superuser or (obj and obj.id == request.user.id)





admin.site.unregister(User)

admin.site.register(User, UserAdmin)