from django.conf.urls import url
from . import views

urlpatterns = [
     
    url(
        r'^$listquestions',
        views.ListQuestionsView.as_view(),
        name="listquestions"
    ),
]