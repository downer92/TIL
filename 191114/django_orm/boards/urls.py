from django.urls import path
from . import views # 현재 폴더에 있는 views를 import 하겠다.

urlpatterns = [
    path('', views.index), # views 안에 index가 없기 때문에 views.py에서 index 정의
    path('subway_order/', views.subway_order),
    path('reciept/', views.reciept),
    path('id_order/id=<int:id>', views.id_order),
]