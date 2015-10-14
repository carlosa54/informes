from django.db import models
from ..utils.models import BaseModel
from ..departamentos.models import Departamento, Answer
from ..users.models import User
from datetime import datetime


# Create your models here.
class Informe(BaseModel):
	name = models.CharField(max_length=200)
	user = models.ForeignKey(User)
	departamentos = models.ManyToManyField(Departamento, through='InformeDepartamento')
	questions = models.ManyToManyField(Answer, through='InformeQuestion')
	date = models.DateField(default = datetime.now)

	def __unicode__(self):
		return self.name + ' : ' + self.user.regional

class InformeDepartamento(BaseModel):
	departamento = models.ForeignKey(Departamento)
	informe = models.ForeignKey(Informe)

class InformeQuestion(BaseModel):
	informe = models.ForeignKey(Informe)
	question = models.ForeignKey(Answer)