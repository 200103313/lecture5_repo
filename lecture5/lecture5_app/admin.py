from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Lecture5_app)
admin.site.register(Sport)
admin.site.register(Categories)
class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
admin.site.register(Posts, PostsAdmin)
admin.site.register(Cities)