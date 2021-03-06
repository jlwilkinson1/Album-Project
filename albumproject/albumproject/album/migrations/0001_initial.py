# Generated by Django 3.1.7 on 2021-03-10 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_description', models.CharField(max_length=200)),
                ('album_name', models.TextField()),
                ('album_release', models.DateField()),
                ('album_time', models.TextField()),
                ('artist_name', models.TextField()),
            ],
        ),
    ]
