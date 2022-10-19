# todo/todo/urls.py : Main urls.py
# from django.conf.urls import url
from django.urls import re_path, include

from .views import (
    TodoListApiView,
    ScrapperApiView
)

urlpatterns = [
    re_path('api', TodoListApiView.as_view()),
    re_path('scrap', ScrapperApiView.as_view()),
]