from django.urls import path
from django.conf.urls import url
import blog.views

urlpatterns = [
    path('', blog.views.index),
]
