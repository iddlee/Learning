# Generated by Django 2.0.6 on 2018-08-16 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('score', models.FloatField()),
            ],
        ),
    ]
