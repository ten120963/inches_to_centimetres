from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),  
	path('ic.html', views.ic, name="ic"),
	path('ci.html', views.ci, name="ci"), 
]
