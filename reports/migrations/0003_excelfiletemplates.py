# Generated by Django 3.1.5 on 2021-01-22 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20210122_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFileTemplates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel_file', models.FileField(upload_to='excel_file_templates')),
            ],
        ),
    ]
