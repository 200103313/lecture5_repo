# Generated by Django 4.0.3 on 2022-04-13 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture5_app', '0005_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='posts',
            name='is_published',
        ),
        migrations.AddField(
            model_name='posts',
            name='age',
            field=models.IntegerField(default=19, verbose_name='Возраст'),
        ),
        migrations.AddField(
            model_name='posts',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email-адрес'),
        ),
        migrations.AddField(
            model_name='posts',
            name='living',
            field=models.BooleanField(default=True, verbose_name='Живет в КЗ'),
        ),
        migrations.AddField(
            model_name='posts',
            name='nationality',
            field=models.CharField(default='kazakh', max_length=255, verbose_name='Национальность'),
        ),
        migrations.AddField(
            model_name='posts',
            name='surname',
            field=models.CharField(default='-', max_length=255, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
    ]
