from pydoc import describe
from pyexpat import model
from django.db import models
from django.urls import reverse

# Create your models here.
class Lecture5_app(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    picture = models.ImageField(default='default value')
    author = models.CharField(max_length=30, default="anon")
    email = models.EmailField(blank=True)
    describe = models.TextField(default='DataFlair Django tutorials')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рассказ"
        verbose_name_plural = "Рассказы"
        ordering = ['-author', 'title']

class Sport(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(default='default value')
    author = models.CharField(max_length=30, default="anon")
    email = models.EmailField(blank=True)
    describe = models.TextField(default='DataFlair Django tutorials')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Спорт"
        verbose_name_plural = "Спортсмены"
        ordering = ['-author', 'title']

#class Login(models.Model):
    #name = models.CharField(max_length=30, default="anon")
    #email = models.EmailField(blank=True)

    #def __str__(self):
        #return self.title

    #class Meta:
        #verbose_name = "Пользователи"
        #verbose_name_plural = "Пользователи"


class Categories(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    picture = models.ImageField(default='default value')
    describe = models.TextField(default='DataFlair Django tutorials')

class Cities(models.Model):
    title = models.CharField(max_length=255)

class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(default = '-', max_length=255, verbose_name="Фамилия")
    age = models.IntegerField(default=19, verbose_name="Возраст")
    nationality = models.CharField(default = 'kazakh', max_length=255, verbose_name="Национальность")
    email = models.EmailField(blank=True, verbose_name="Email-адрес")
    living = models.BooleanField(default=True, verbose_name="Живет в КЗ")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('post', kwargs = {'post_slug': self.slug })
    
    def __str__(self):
        return self.title
    
    class Meta:
        get_latest_by = ['title']

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)