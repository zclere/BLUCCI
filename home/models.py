from django.db import models
from magazine.models import *
# Create your models here.

class FeaturedContent(models.Model):
	featured_content = models.ForeignKey(ContentList, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=200, null=True, blank=True)
	seo_description = models.TextField(verbose_name="SEO Description", null=True, blank=False)
	featured = models.BooleanField(default=False)
	position_choices = [('left', 'left'), ('right', 'right')]
	grid_position = models.CharField(choices=position_choices, max_length=6, null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		verbose_name = 'Featured Content'
		verbose_name_plural = 'Featured Content'

	def __str__(self):
		return self.title