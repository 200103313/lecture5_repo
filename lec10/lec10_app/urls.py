from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>', views.show_post, name='post')
]