from django.urls import path
from . import views


# https://docs.djangoproject.com/en/dev/topics/http/urls/#url-dispatcher

urlpatterns = [
    path('', views.post_list, name='post_list'),
]