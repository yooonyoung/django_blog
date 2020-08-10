from django.db import models
from django.utils import timezone

class YY_Post(models.Model):
    # 작성자
    writer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # 제목
    title = models.CharField(max_length=200)
    # 내용
    text = models.TextField()
    # 작성일자
    created_date = models.DateTimeField(default=timezone.now)
    # 게시일자
    published_date = models.DateTimeField(blank=True, null=True)

    # 게시일자에 현재날짜시간을 대입해주는 함수
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # 객체주소 대신 글제목을 반환해주는 toString() 함수
    def __str__(self):
        return self.title + '랄라'