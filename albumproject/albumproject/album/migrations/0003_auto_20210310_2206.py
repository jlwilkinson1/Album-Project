# Generated by Django 3.1.7 on 2021-03-11 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20210310_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_description',
            field=models.TextField(max_length=400),
        ),
    ]