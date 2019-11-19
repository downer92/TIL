from django.urls import path
from . import views 

app_name = "board"
urlpatterns = [
    path('new/', views.new, name="new"),
    # path('/', views.index, name="index"),
    path('', views.index, name="index"),
    path('<int:pk>/detail/', views.detail, name="detail"),
    path('<int:pk>/snew/', views.snew, name="snew"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/update/', views.update, name="update"),
    path('<int:pk>/sdelete/', views.sdelete, name="sdelete"),
    path('<int:pk>/vote/', views.vote, name="vote")

]