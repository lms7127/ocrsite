# Generated by Django 4.2.3 on 2023-07-24 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inpimg', '0002_profile_delete_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lan', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='title',
        ),
    ]
