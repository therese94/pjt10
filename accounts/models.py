from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# User 모델을 Customizing 한다.
# default user model을 사용하더라도 확장성을 위해서 customizing 한다.
class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name = 'follwings'      # 역참조를 위해서 필요한것
    )

    
    
