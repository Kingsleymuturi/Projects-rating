# Generated by Django 2.0.2 on 2020-08-16 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='company',
        ),
    ]
