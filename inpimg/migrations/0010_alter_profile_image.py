# Generated by Django 4.2.3 on 2023-07-27 10:08

from django.db import migrations, models
import inpimg.models


class Migration(migrations.Migration):

    dependencies = [
        ('inpimg', '0009_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to=inpimg.models.Profile.upload_to_func),
        ),
    ]