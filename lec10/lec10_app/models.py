from django.db import models

# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=255, verbose_name="Takyryp")
    is_published = models.BooleanField(default=True, verbose_name="Shygarshylym")