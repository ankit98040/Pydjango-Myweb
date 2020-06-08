# Generated by Django 3.0.6 on 2020-06-06 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0008_songs_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
