from django.conf.urls import url
from . import views

urlpatterns = [
     
    url(
        r'^departamentos/',
        views.DepartamentosView.as_view(),
        name="departamentos"
    ),
]