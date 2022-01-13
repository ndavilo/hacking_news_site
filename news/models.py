from django.db import models
from django.urls import reverse


class News(models.Model):
	heading = models.CharField(max_length=50, default='Heading here')
	date 	= models.DateTimeField(auto_now_add=True)
	body	= models.TextField(default='Body of this text')
	source	= models.CharField(max_length=50, default='anonymous')
	def __str__(self):
		return self.source + ': ' + self.heading

	def get_absolute_url(self):
		return reverse('article-detail', args=[str(self.id)])

class Comment(models.Model):
	post 	= models.ForeignKey(News, related_name="comments", on_delete=models.CASCADE)
	name 	= models.CharField(max_length=50, default='anonymous')
	body	= models.TextField(default='Body of this text')
	date 	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' %(self.post.heading, self.name)
