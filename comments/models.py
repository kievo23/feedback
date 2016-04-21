from __future__ import unicode_literals

from django.db import models
from companies.models import Company 

# Create your models here.
class Comment (models.Model):
	first_name = models.CharField(max_length = 150)
	second_name = models.CharField(max_length = 150)
	phone = models.CharField(max_length = 150)
	comment = models.TextField(max_length = 1500)
	company_id = models.ForeignKey(Company,on_delete=models.CASCADE,default='')
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	def __unicode__(self):
		return self.comment
