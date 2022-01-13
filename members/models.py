from django.db import models

from django.urls import reverse

class Member(models.Model):
	firstname	=	models.CharField(max_length=50, default='First name here')
	othernames	=	models.CharField(max_length=50, default='Other names here')
	age 		=	models.IntegerField()
	email 		=	models.EmailField(max_length=100, default='email address here')
	passwd      =	models.CharField(max_length=50, default='Password here')
	
	def __str__(self):
		return self.firstname + ' ' + self.othernames