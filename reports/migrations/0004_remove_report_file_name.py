# Generated by Django 3.1.5 on 2021-02-05 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20210205_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='file_name',
        ),
    ]
