from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view-all/', views.view_all, name='view_all'),
]