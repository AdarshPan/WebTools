# Generated by Django 2.1 on 2019-03-27 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctgctg', '0023_music'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='user_uploaded',
        ),
        migrations.DeleteModel(
            name='Music',
        ),
    ]
