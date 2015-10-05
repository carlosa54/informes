from django.contrib import admin
from .models import Departamento, Answer, DepartamentoQuestion, DepartamentoPerson
# Register your models here.
admin.site.register(Departamento)
admin.site.register(Answer)
admin.site.register(DepartamentoQuestion)
admin.site.register(DepartamentoPerson)