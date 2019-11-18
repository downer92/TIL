from django.urls import path
from . import views

app_name = "subway" # path 이름이 겹쳐서 name space를 사용할 때 문제가 생길 경우를 대비해 appname을 설정해 줄 수 있다. 
urlpatterns = [
    # name을 설정하면 url 관리가 수월하다.
    # {% url 'app_name:설정name' %} 방식으로 사용
    # url이 바뀌어도 일일이 찾아서 바꿀 필요가 없다.
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    # path('create/', views.create, name='create'),
    # {% url 'app_name:설정name' 넘길데이터1 넘길데이터2 %}
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    # path('<int:pk>/change/', views.change, name='change'),
    path('<int:pk>/delete/', views.delete, name='delete')
]