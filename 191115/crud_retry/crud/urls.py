from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new),
    path('create/', views.create),
    path('', views.index),
    path('<int:pk>/detail/', views.detail),
    path('<int:pk>/update/', views.update),
    path('<int:pk>/revise/', views.revise),
    path('<int:pk>/delete/', views.delete)
]