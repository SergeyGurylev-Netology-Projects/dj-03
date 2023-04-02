from enum import unique

from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='Модель')
    price = models.FloatField(verbose_name='Цена')
    image = models.URLField(max_length=255, verbose_name='Картинка')
    release_date = models.DateField(verbose_name='Дата выпуска')
    lte_exists = models.BooleanField(verbose_name='Есть в наличии')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} {self.name}, цена: {self.price}, дата выпуска: {self.release_date}, есть в наличии: {self.lte_exists}'
