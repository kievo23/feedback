
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class Company (models.Model):
	name = models.CharField(max_length = 150)
	tag_line = models.CharField(max_length = 250)
	logo = models.FileField(upload_to='companies/%Y/%m/%d')
	employee_id = models.ForeignKey(settings.AUTH_USER_MODEL,default='1')
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.name