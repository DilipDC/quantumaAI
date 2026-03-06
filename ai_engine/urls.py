
from django.urls import path
from . import views

urlpatterns = [
path('', views.dashboard),
path('api/process/', views.process_ai),
]
