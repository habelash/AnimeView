from django.db import models


class onepiece(models.Model):
    Episode = models.PositiveIntegerField()
    EpisodeLink = models.URLField(max_length=200)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'One Piece'


class naruto(models.Model):
    Episode = models.PositiveIntegerField()
    EpisodeLink = models.URLField(max_length=200)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'Naruto'


class haikyu(models.Model):
    Episode = models.PositiveIntegerField()
    EpisodeLink = models.URLField(max_length=200)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'Haikyu'


class bleach(models.Model):
    Episode = models.PositiveIntegerField()
    EpisodeLink = models.URLField(max_length=200)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'Bleach'


class aot(models.Model):
    Episode = models.PositiveIntegerField()
    EpisodeLink = models.URLField(max_length=200)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'Attack On Titans'


class deathnote(models.Model):
    Episode = models.PositiveIntegerField()
    EpisodeLink = models.URLField(max_length=200)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'Death Note'


class bnha(models.Model):
    Episode = models.PositiveIntegerField()
    EpisodeLink = models.URLField(max_length=200)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'My Hero Accadamy'


class fmab(models.Model):
    Episode = models.PositiveIntegerField()
    EpisodeLink = models.URLField(max_length=200)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'Full Metal Alchemist Brotherhood'


class afrosamurai(models.Model):
    Episode = models.PositiveIntegerField()
    EpisodeLink = models.URLField(max_length=200)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'Afro Samurai'


class hxh(models.Model):
    Episode = models.PositiveIntegerField()
    EpisodeLink = models.URLField(max_length=200)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'Hunter X Hunter'


class kny(models.Model):
    Episode = models.PositiveIntegerField()
    EpisodeLink = models.URLField(max_length=200)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'Demon Slayer'


class onepunchman(models.Model):
    Episode = models.PositiveIntegerField()
    EpisodeLink = models.URLField(max_length=200)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'One Punch Man'


class fairytail(models.Model):
    Episode = models.PositiveIntegerField()
    EpisodeLink = models.URLField(max_length=200)
    Discription = models.TextField()
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'Fairy Tail'
