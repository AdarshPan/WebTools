# Generated by Django 2.1 on 2019-03-27 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctgctg', '0026_auto_20190327_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='Cover_Picture',
        ),
        migrations.RemoveField(
            model_name='music',
            name='Song_File',
        ),
    ]