from django.urls import path
from blogger import views

urlpatterns = [
	path('', views.index, name='index')
]
