# Generated by Django 3.2.5 on 2021-07-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='posts',
        ),
        migrations.AddField(
            model_name='posts',
            name='tags',
            field=models.ManyToManyField(blank=True, to='myapp.Tags', verbose_name='Статьи'),
        ),
    ]
