from django.contrib import admin
from django.contrib.auth import get_user_model

# 현재 활성화되어있는 유저 모델을 가져오는 함수
User = get_user_model()

admin.site.register(User)

# Register your models here.
