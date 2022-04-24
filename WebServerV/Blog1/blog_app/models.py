from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    comment = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # '관리자 화면에서 post 리스트 를 보일때 [PK]title 값으로 제목을 표시
    # 지금 Post table 은 pk 라는 이름 으로 PK 가 설정 되어 있다.
    def __str__(self):
        return f'[{self.pk}]{self.title}'
    