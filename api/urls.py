from django.urls import path, include

from . import views
 
urlpatterns = [
	path('projects/', views.ProjectListView.as_view()),
	path('projects/<int:pk>/', views.DetailProject.as_view()),
	path('tasks/', views.TaskListView.as_view()),
	path('tasks/<int:pk>/', views.DetailTask.as_view()),

	path('users/', include('users.urls')),
	path('rest-auth/', include('rest_auth.urls')),
	path('rest-auth/registration/', include('rest_auth.registration.urls')),
]