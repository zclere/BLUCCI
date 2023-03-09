from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
# Register your models here.

class DetailedMagazineAdmin(admin.StackedInline):
	model = DetailedMagazine
	extra = 1

	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


class ContentListAdmin(admin.ModelAdmin):
	inlines = [DetailedMagazineAdmin]

	list_display = ["title", "magazine", "date_published"]


	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)


	def get_exclude(self, request, obj=None):
		excluded = super().get_exclude(request, obj) or [] # get overall excluded fields

		if not request.user.is_superuser: # if user is not a superuser
			return excluded + ['user']

		return excluded # otherwise return the default excluded fields if any


	#only lets one view stuff they created and not stuff created by other people
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		user = request.user
		return qs if user.is_superuser else qs.filter(user=user)

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == "magazine":
			kwargs["queryset"] = Magazine.objects.filter(user=request.user)
		return super(ContentListAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

	def has_add_permission(self, request):
		num_objects = self.model.objects.filter(user=request.user).count()
		if num_objects >= 20:
			return False
		else:
			return True

	def has_delete_permission(self, request, obj=None):
		return True




class MagazineAdmin(admin.ModelAdmin):

	list_display = ["name", "genre_category"]

	def genre_category(self, obj):
		return "\n".join(['#' + m.name for m in obj.magazine_type.all()])


	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)


	def get_exclude(self, request, obj=None):
		excluded = super().get_exclude(request, obj) or [] # get overall excluded fields

		if not request.user.is_superuser: # if user is not a superuser
			return excluded + ['user']

		return excluded # otherwise return the default excluded fields if any


	#only lets one view stuff they created and not stuff created by other people
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		user = request.user
		return qs if user.is_superuser else qs.filter(user=user)


	def formfield_for_manytomany(self, db_field, request, **kwargs):
		if db_field.name == "magazine_type":
			kwargs["queryset"] = Genre.objects.filter(user=request.user)
		return super(MagazineAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


	def has_add_permission(self, request):
		num_objects = self.model.objects.filter(user=request.user).count()
		if num_objects >= 10:
			return False
		else:
			return True

	def has_delete_permission(self, request, obj=None):
		return True

class GenreAdmin(admin.ModelAdmin):

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)


	def get_exclude(self, request, obj=None):
		excluded = super().get_exclude(request, obj) or [] # get overall excluded fields

		if not request.user.is_superuser: # if user is not a superuser
			return excluded + ['user']

		return excluded # otherwise return the default excluded fields if any


	#only lets one view stuff they created and not stuff created by other people
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		user = request.user
		return qs if user.is_superuser else qs.filter(user=user)

	def has_add_permission(self, request):
		num_objects = self.model.objects.filter(user=request.user).count()
		if num_objects >= 5:
			return False
		else:
			return True

admin.site.register(Genre, GenreAdmin)

admin.site.register(Magazine, MagazineAdmin)

admin.site.register(ContentList, ContentListAdmin)
