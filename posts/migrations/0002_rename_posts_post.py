# Generated by Django 4.0.1 on 2022-01-28 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='posts',
            new_name='post',
        ),
    ]