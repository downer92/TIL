from django.db import models
   
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length =50) #기사 제목 / 문자열
    content = models.TextField() #기사 내용
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) # editable option => False 
   
    def __str__(self):
        return f'{self.id} : {self.title}'

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    # ForeignKey(어떤 테이블을 참조할지, 그 테이블이 삭제될 때 어떻게 할지)
    # models.CASCADE : 부모 테이블 삭제시 같이 삭제하는 옵션
    # models.PROTECT : 부모 테이블이 삭제될 때 오류 발생
    # models.SET_NULL : 삭제되었을 때, 부모 참조 값을 NULL값으로 채움. 단, NOT NULL 옵션인 경우에는 불가능
    # models.SET() : 특정 함수를 호출
    # models.DO_NOTHING : 아무것도 안함
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
