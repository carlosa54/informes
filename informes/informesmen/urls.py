from django.conf.urls import url
from . import views

urlpatterns = [
     
    url(
        r'^$',
        views.DashBoardView.as_view(),
        name="dashboard"
    ),
    url(
        r'^createinforme/',
        views.CreateInformeView.as_view(),
        name="createinforme"
    ),
    url(
        r'^listinformes/',
        views.ListInformesView.as_view(),
        name="listinformes"
    ),
]