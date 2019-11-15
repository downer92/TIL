from django.urls import path
from . import views 

urlpatterns = [
    
    path('new/', views.new), #crud/new/
    path('create/', views.create), #crud/create/
    path('', views.index), #crud/
    # crud/pk/article/ detail page
    path('<int:pk>/article/', views.detail), # 해당 url로 가면 views.detail 실행하겠다!
    # crud/pk/update/ 수정 페이지
    path('<int:pk>/update/', views.update),
    # crud/pk/revise/ 최종 업데이트
    path('<int:pk>/revise/', views.revise),
    # crud/pk/delete/ 삭제하기
    path('<int:pk>/delete/', views.delete),
]