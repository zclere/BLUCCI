from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


class Genre(models.Model):
	name = models.CharField(max_length=70, blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

	class Meta:
		verbose_name = 'Genre'
		verbose_name_plural = 'Genre'


	def __str__(self):
		return self.name



class Magazine(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	image = models.ImageField(null=True, blank=True, upload_to='all_magazines/')
	magazine_slug = models.SlugField(verbose_name='slug', unique=True, null=True, blank=True)
	magazine_type = models.ManyToManyField(Genre, verbose_name="genre")
	user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


	class Meta:
		verbose_name = 'Magazines'
		verbose_name_plural = 'Magazines'


	def save(self, *args, **kwargs):
		if self.magazine_slug is None:
			self.magazine_slug = slugify(self.name)
		super().save(*args, **kwargs)


	@property
	def image_URL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url 

	def __str__(self):
		return self.name


class ContentList(models.Model):

	title = models.CharField(max_length=150, blank=True, null=True)
	image = models.ImageField(null=True, blank=True, upload_to='magazine_images/')
	date_published = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=50, null=True, blank=True)
	content_slug = models.SlugField(verbose_name='slug', unique=True, null=True, blank=True)
	magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


	class Meta:
		verbose_name = 'Writings'
		verbose_name_plural = 'Writings'


	def save(self, *args, **kwargs):
		if self.content_slug is None:
			self.content_slug = slugify(self.title)
		super().save(*args, **kwargs)


	@property
	def image_URL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url 


	def __str__(self):
		return self.title


class DetailedMagazine(models.Model):

	title = models.CharField(max_length=400, null=True, blank=True)
	image = models.ImageField(null=True, blank=True, upload_to='magazine_images/detailed_images/')
	description = models.TextField()

	contentlist = models.ForeignKey(ContentList, on_delete=models.CASCADE)


	class Meta:
		verbose_name = 'Magazine Content'
		verbose_name_plural = 'Magazine Content'


	@property
	def image_URL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url


	def __str__(self):
		return self.title