# Generated by Django 2.1 on 2019-02-12 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctgctg', '0008_members_scores'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='username',
            new_name='username_for_site',
        ),
    ]
