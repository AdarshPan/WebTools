# Generated by Django 2.1 on 2019-03-26 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctgctg', '0019_music'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='Description',
            field=models.TextField(blank=True),
        ),
    ]