from django.db import models
from ..utils.models import BaseModel
from ..questions.models import Question
from ..persons.models import Person
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Departamento(BaseModel):
	name = models.CharField(max_length=200)
	questions = models.ManyToManyField(Question, through='DepartamentoQuestion')
	personas = models.ManyToManyField(Person, through='DepartamentoPerson')

	def __unicode__(self):
		return self.name

class DepartamentoQuestion(BaseModel):
	departamento = models.ForeignKey(Departamento)
	question = models.ForeignKey(Question)


class DepartamentoPerson(BaseModel):
	departamento = models.ForeignKey(Departamento)
	persona = models.ForeignKey(Person)
	def __unicode__(self):
		return self.persona.first_name

class Answer(BaseModel):
	number = models.IntegerField(validators= [MinValueValidator(0)])
	pregunta = models.ForeignKey(DepartamentoQuestion)
	persona = models.ForeignKey(Person)
	def __unicode__(self):
		return str(self.number)
