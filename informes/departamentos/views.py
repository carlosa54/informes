from django.shortcuts import redirect
from django.views.generic import TemplateView 
from .models import Departamento
# Create your views here.
class DepartamentosView(TemplateView):
	template_name = "dashboard/listDepartamentos.html"

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)
		
		return self.render_to_response(context)

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)
		print request.session['informe_id']

		context = self.retrieve_departamentos(request.user, context)
		return self.render_to_response(context)

	def retrieve_departamentos(self,user,context):
		departamentos = Departamento.objects.all()
		context["departamentos"] = departamentos
		return context
