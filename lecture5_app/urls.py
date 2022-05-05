from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('posts.urls')),
    path('home/', views.home, name = "home"),
    path('', views.index, name = "index"),
    path('nature/', views.nature, name = "nature"),
    path('sport/', views.sport, name = "sport"),
    path('food/', views.food, name = "food"),
    path('art/', views.art, name = "art"),
    path('traditions/', views.traditions, name = "traditions"),
    path('upload/', views.upload, name = "upload-posts"),
    path('update/<int:post_id>', views.update_post),
    path('delete/<int:post_id>', views.delete_post),
    path('polls/', views.polls),
    path('post/<slug:post_slug>', views.show_post, name='post'),
    path('addpage/', views.addpage, name='add_page'),
    path('send/', views.send_message),
    path('welcome/', views.welcome, name = "welcome")
]
