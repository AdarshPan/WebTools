# Generated by Django 2.1 on 2019-03-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctgctg', '0012_auto_20190324_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='File',
            field=models.FileField(upload_to='media'),
        ),
    ]