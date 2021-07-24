from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название поста')
    content = models.TextField(blank=True, verbose_name='Текст поста')
    photo = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Фото')
    quote = models.TextField(verbose_name='Цитата')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    tags = models.ManyToManyField('Tags', blank=True, verbose_name='Теги')

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tags(models.Model):
    name = models.CharField(max_length=150, verbose_name='Тег')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class FeedBack(models.Model):
    user = models.CharField(max_length=150, verbose_name='Отправитель', blank=False)
    email = models.EmailField(max_length=100, verbose_name='Email отправителя', blank=False)
    message = models.TextField(verbose_name='Текст обращения', blank=False)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
