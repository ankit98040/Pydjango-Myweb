# Generated by Django 3.0.6 on 2020-06-01 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0004_songs_album_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='album_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Music.Album'),
        ),
    ]