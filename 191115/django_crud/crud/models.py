from django.db import models
   
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length =50) #기사 제목 / 문자열
    content = models.TextField() #기사 내용
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) # editable option => False 
   
    def __str__(self):
        return f'{self.id} : {self.title}'
