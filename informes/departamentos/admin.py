from django.contrib import admin
from .models import Departamento, Answer, DepartamentoQuestion, DepartamentoPerson
# Register your models here.
class QuestionInlineAdmin(admin.TabularInline):
    model = Departamento.questions.through

class PersonInlineAdmin(admin.TabularInline):
	model = Departamento.personas.through


class DepartamentoAdmin(admin.ModelAdmin):
    inlines = (QuestionInlineAdmin,PersonInlineAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Answer)
