from django.urls import path
from django.conf.urls import url, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, base_name='posts_view')

app_name = 'zipariblog'
urlpatterns = [
	path('', views.index, name='index'),
	path('new/', views.create, name='create'),
	path('submit/', views.submit, name='submit'),
	path('<int:post_id>/', views.detail, name='detail'),
	path('<int:post_id>/edit/', views.edit, name='edit'),
	path('<int:post_id>/submit', views.submit_edit, name='submit_edit'),

	url(r'^', include(router.urls)),
]