# Generated by Django 3.1.5 on 2021-01-25 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_excelfiletemplates'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExcelFileTemplates',
            new_name='ExcelFileTemplate',
        ),
    ]
