# Generated by Django 4.2.3 on 2023-07-25 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inpimg', '0003_language_remove_profile_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Language',
        ),
    ]