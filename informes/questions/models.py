from django.db import models
from ..utils.models import BaseModel
from ..persons.models import Person
# Create your models here.

class Question(BaseModel):
	question_text = models.CharField(max_length=200)

	def __unicode__(self):
		return self.question_text	