from django.contrib import admin
from .models import Board # 현재 폴더 안에 있는 models의 Board를 import

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    fields = ['content', 'title'] # 필드 순서를 바꿔서 적용
    list_display = ['title', 'updated_at'] # 보고 싶은 컬럼명을 적어주면 해당 컬럼명이 위에 나타나게 된다.
    list_filter = ['updated_at']
    search_fields = ['title', 'content'] # 검색하고자 하는 컬럼명을 [] 안에 넣어주면 됨

admin.site.register(Board, BoardAdmin) # 저장을 할 때 뒤에 BoardAdmin을 추가해주면 페이지까지 적용이 된다.