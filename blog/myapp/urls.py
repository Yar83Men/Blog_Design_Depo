from django.urls import path, include
from .views import *

urlpatterns = [
    path('', posts_all, name="home"),
    path('sort/date/', sort_by_date, name='sort_by_date'),
    path('sort/category/', sort_by_category, name='sort_by_category'),
    path('sort/tag/', sort_by_tag, name='sort_by_tag'),
    path('post/detail/<int:post_id>', post_detail, name='post_detail'),
    path('feedback/', feedback, name='feedback')
]
