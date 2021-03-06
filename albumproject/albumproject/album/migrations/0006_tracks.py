# Generated by Django 3.1.7 on 2021-03-13 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_auto_20210311_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_number', models.CharField(max_length=510)),
                ('track_name', models.CharField(max_length=25)),
                ('track_time', models.CharField(max_length=25)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.album')),
            ],
        ),
    ]
