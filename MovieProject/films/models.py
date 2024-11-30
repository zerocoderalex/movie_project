from django.db import models

# Create your models here.
class News_post(models.Model):
        title = models.CharField('Название фильма', max_length=150)
        short_description = models.TextField('Описание фильма')
        text = models.TextField('Отзыв')

        def __str__(self):
            return self.title

        class Meta:
            verbose_name = 'Фильм'
            verbose_name_plural = 'Фильмы'



