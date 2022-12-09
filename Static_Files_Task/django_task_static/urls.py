from django_task_static import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index')
]