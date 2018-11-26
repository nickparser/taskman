from django.urls import path

from . import views
from taskman import celerytask

urlpatterns = [
	path('', views.index),
	path('send/', views.send)
]