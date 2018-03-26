from django.urls import path

from . import views

app_name = 'zipariblog'
urlpatterns = [
	path('', views.index, name='index'),
	path('new/', views.create, name='create'),
	path('submit/', views.submit, name='submit'),
	path('<int:post_id>/', views.detail, name='detail'),
	path('<int:post_id>/edit/', views.edit, name='edit'),
	path('<int:post_id>/submit', views.submit_edit, name='submit_edit')
]