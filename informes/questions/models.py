from django.db import models
from ..utils.models import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Answer(BaseModel):
	number = models.IntegerField(validators= [MinValueValidator(0)])
	def __unicode__(self):
		return str(self.number)

class Question(BaseModel):
	question_text = models.CharField(max_length=200)
	answer = models.ForeignKey(Answer, null=True, blank=True)

	def __unicode__(self):
		return self.question_text	