
from django.urls import path
from . import views

urlpatterns = [
path('', views.dashboard, name="dashboard"),
path('api/process/', views.process_ai, name="process_ai"),
]
