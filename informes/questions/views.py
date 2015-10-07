from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ListQuestionsView(TemplateView):
	template_name = 'dashboard/listQuestion.html'

	def post(self,request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")

		