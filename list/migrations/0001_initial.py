# Generated by Django 3.0.6 on 2020-06-10 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='animelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Discription', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
            ],
            options={
                'verbose_name_plural': 'Anime List',
            },
        ),
        migrations.CreateModel(
            name='topanime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Discription', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
            ],
            options={
                'verbose_name_plural': 'Top Anime',
            },
        ),
    ]
