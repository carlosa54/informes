from django.db import models
from ..utils.models import BaseModel
from ..departamentos.models import Departamento
from ..users.models import User

# Create your models here.
class Informe(BaseModel):
	name = models.CharField(max_length=200)
	user = models.ForeignKey(User)
	departamentos = models.ManyToManyField(Departamento, through='InformeDepartamento')

class InformeDepartamento(BaseModel):
	departamento = models.ForeignKey(Departamento)
	informe = models.ForeignKey(Informe)