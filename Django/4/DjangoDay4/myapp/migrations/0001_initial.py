# Generated by Django 2.0.6 on 2018-08-09 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('capital', models.CharField(max_length=20)),
                ('king', models.CharField(max_length=10)),
            ],
        ),
    ]