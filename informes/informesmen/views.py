from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from ..persons.models import Person
from .models import Informe
from ..questions.models import Question
from ..departamentos.models import Departamento
from .forms import InformeForm
# Create your views here.

class CreateInformeView(TemplateView):
	template_name = 'dashboard/createInforme.html'

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)
		form = InformeForm()

		if request.POST.get("departamento", False):
			context["departamento"] = request.POST.get("departamento", False)
			context = self.retrieve_persons(request.user,context)

		if form.is_valid():
			new_informe = form.save(commit=False)
			new_informe.user = request.user
		context = self.retrieve_persons(request.user,context)
		return self.render_to_response(context)

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)
		form = InformeForm()

		context["form"] = form

		#context = self.retrieve_persons(request.user, context)
		return self.render_to_response(context)



	def retrieve_persons(self, user, context):
		persons = Person.objects.filter(regional=user.regional, departamento__name = context["departamento"])
		questions = Question.objects.filter(departamento__name = context["departamento"])
		context["questions"] = questions
		context["persons"] = persons
		
		return context



class ListInformesView(TemplateView):
	template_name = "dashboard/listInformes.html"

	def get(self,request,*args, **kwargs):
		if not request.user.is_authenticated():
			return redirect('/login')
		context = self.get_context_data(**kwargs)

		informes = Informe.objects.filter(user=request.user).order_by('created_at')

		context['informes'] = informes

		return self.render_to_response(context)


class DashBoardView(TemplateView):
    template_name = "dashboard/listDepartamentos.html"

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect("/login")
        context = self.get_context_data(**kwargs)
        form = InformeForm(request.POST)

        if form.is_valid():
            new_informe = form.save(commit=False)
            new_informe.user = request.user



            context["success"] = "The Invoice was sent to the user"
        else:
            context["error"] = "The Invoice failed to be created."

        context = self.retrieve_departamentos_and_persons(request.user, context)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect("/login")
        context = self.get_context_data(**kwargs)

        context = self.retrieve_departamentos_and_persons(request.user, context)
        return self.render_to_response(context)

    def retrieve_departamentos_and_persons(self, user, context):
    	persons = Person.objects.filter(regional=user.regional)
    	departamentos = Departamento.objects.all()
    	context["persons"] = persons
    	context["departamentos"] = departamentos
    	return context