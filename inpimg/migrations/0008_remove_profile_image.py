# Generated by Django 4.2.3 on 2023-07-25 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inpimg', '0007_profile_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]