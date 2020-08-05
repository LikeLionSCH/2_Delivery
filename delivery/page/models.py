from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50) #주문자 성명
    address = models.TextField() #주문자 주소
    store = models.CharField(max_length=50) #가게 이름
    menu = models.CharField(max_length=50) #메뉴
    option = models.TextField() #부수적인 옵션

    def __str__(self):
        return self.name