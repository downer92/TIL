from django.db import models

# Create your models here.
class Subway(models.Model):
    name = models.CharField(max_length=15)
    address = models.TextField()
    phone = models.TextField()
    menu = models.TextField()
    bread = models.TextField()
    vegetable = models.TextField()
    sauce = models.TextField()
    drink = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f'{self.name} : {self.menu}'