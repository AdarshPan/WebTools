# Generated by Django 2.1 on 2019-02-11 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctgctg', '0006_auto_20190211_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scores',
            name='name',
        ),
        migrations.DeleteModel(
            name='Members',
        ),
        migrations.DeleteModel(
            name='Scores',
        ),
    ]
