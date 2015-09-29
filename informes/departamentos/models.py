from django.db import models
from ..utils.models import BaseModel
from ..questions.models import Question
from ..persons.models import Person
# Create your models here.
class Departamento(BaseModel):
	name = models.CharField(max_length=200)
	questions = models.ManyToManyField(Question)
	personas = models.ManyToManyField(Person)

	def __unicode__(self):
		return self.name