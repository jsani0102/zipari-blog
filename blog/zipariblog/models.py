from django.db import models

# Create your models here.
class Post(models.Model):
	author = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	content = models.TextField()
	created_at = models.DateTimeField('time created')

	def __str__(self):
		return self.content
