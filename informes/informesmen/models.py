from django.db import models
from ..utils.models import BaseModel
from ..departamentos.models import Departamento
from ..users.models import User

# Create your models here.
class Informe(BaseModel):
	name = models.CharField(max_length=200)
	user = models.ForeignKey(User)
	departamentos = models.ManyToManyField(Departamento)
