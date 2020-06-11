from django.db import models


# Create your models here.

class animelist(models.Model):
    name = models.CharField(max_length=50)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'Anime List'


class topanime(models.Model):
    name = models.CharField(max_length=50)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'Top Anime'
