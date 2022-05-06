from cProfile import label
from dataclasses import fields
import datetime
from turtle import title
from django import forms
from .models import *

class PostCreate(forms.ModelForm):
    class Meta:
        model = Lecture5_app
        fields = '__all__'

class PostCreateSp(forms.ModelForm):
    class Meta:
        model = Sport
        fields = '__all__'

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label="Имя", widget=forms.TextInput(attrs={'class':'form-input'}))
    surname = forms.CharField(max_length=255, label="Фамилия")
    age = forms.IntegerField(label="Возраст")
    nationality = forms.CharField(max_length=255, label="Национальность")
    email = forms.EmailField(label="Email-адрес")
    living = forms.BooleanField(label="Живете в Казахстане?", required=False, initial=True)
    slug = forms.SlugField(max_length=255, label="URL")
    #city = forms.ModelChoiceField(queryset=Cities)
    #describe = forms.TextField(default='DataFlair Django tutorials')

class RenewBookForm(forms.Form):
    """
    Форма обновления книг для библиотекарей
    """
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        #Проверка, что дата не в прошлом.
        if data < datetime.date.today():
            raise forms.ValidationError(('Invalid date - renewal in past'))
        #Если дата в "далёком" будущем (+4 недели)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise forms.ValidationError(('Invalid date - renewal more than 4 weeks ahead'))

        # Всегда надо возвращать очищенные данные.
        return data
    