# Generated by Django 4.0 on 2021-12-18 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Task',
        ),
    ]