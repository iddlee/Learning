# Generated by Django 2.0.6 on 2018-08-10 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manytomanyapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relation',
            old_name='subject',
            new_name='sub',
        ),
    ]
