# Generated by Django 3.1.7 on 2021-03-11 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_image',
            field=models.ImageField(default='C:\\Users\\jlwil\\albumproject\\albumproject\\albumproject\\album\\defaultimage.jpg', upload_to='album'),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_time',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist_name',
            field=models.CharField(max_length=200),
        ),
    ]
