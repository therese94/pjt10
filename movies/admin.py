from django.contrib import admin
from .models import Genre, Movie, Review

# 장고 어드민 페이지에서 내가 만든 모델을 확인해 볼 수 있다
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Review)

# Register your models here.
