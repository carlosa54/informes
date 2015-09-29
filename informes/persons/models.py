from django.db import models
from ..utils.models import BaseModel
from .constants import REGIONAL_CHOICES
# Create your models here.
class Person(BaseModel):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	regional = models.CharField(max_length=50, choices=REGIONAL_CHOICES, default='sanjuan')

	def __unicode__(self):
		return self.first_name + " " + self.last_name

	@property
	def full_name(self):
		"""
		Returns the first_name plus the last_name, with a space in between.
		"""
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()