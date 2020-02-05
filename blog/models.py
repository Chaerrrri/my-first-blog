from django.db import models
from django.utils import timezone

#모델(object) 정의
class Post(models.Model): #class: 객체 정의, Post: 모델 이름, models: 장고 모델임을 명시 -> Post를 DB에 저장해야 함을 알게 됨
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def publish(self): #publish method 
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
