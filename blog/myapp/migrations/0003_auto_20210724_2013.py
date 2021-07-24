# Generated by Django 3.2.5 on 2021-07-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210723_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150, verbose_name='Отправитель')),
                ('email', models.EmailField(max_length=100, verbose_name='Email отправителя')),
                ('message', models.TextField(verbose_name='Текст обращения')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.AlterField(
            model_name='posts',
            name='tags',
            field=models.ManyToManyField(blank=True, to='myapp.Tags', verbose_name='Теги'),
        ),
    ]