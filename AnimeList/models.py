from django.db import models


# Create your models here.
class onepiece(models.Model):
    Episode = models.PositiveIntegerField()
    EpisodeLink = models.URLField(max_length=200)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'One Piece'

