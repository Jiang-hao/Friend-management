# Generated by Django 2.0.2 on 2018-03-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180305_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendship',
            name='id',
        ),
        migrations.AlterField(
            model_name='friendship',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
