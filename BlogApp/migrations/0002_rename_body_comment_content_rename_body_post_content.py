# Generated by Django 4.0.5 on 2022-06-03 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='content',
        ),
    ]