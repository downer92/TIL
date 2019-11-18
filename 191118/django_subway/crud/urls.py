from django.urls import path
from . import views 

app_name = "crud"
urlpatterns = [
    path('new/', views.new, name='new'), #crud/new/
    # path('create/', views.create, name='create'), #crud/create/
    path('', views.index, name='index'), #crud/
    # crud/pk/article/ detail page
    path('<int:pk>/detail/', views.detail, name='detail'), # 해당 url로 가면 views.detail 실행하겠다!
    # crud/pk/update/ 수정 페이지
    path('<int:pk>/update/', views.update, name='update'),
    # crud/pk/revise/ 최종 업데이트
    # path('<int:pk>/revise/', views.revise, name='revise'),
    # crud/pk/delete/ 삭제하기
    path('<int:pk>/delete/', views.delete, name='delete'),
]