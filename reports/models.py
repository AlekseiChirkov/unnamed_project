from django.db import models

from users.models import User


class ExcelFileTemplate(models.Model):
    excel_file = models.FileField(upload_to='excel_file_templates')
    file_name = models.CharField(max_length=64, default='')

    def __str__(self):
        return f'{self.excel_file}'


class ExcelFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    excel_file = models.FileField(upload_to='excel_files', blank=True, null=True)
    file_name = models.CharField(max_length=64, default='')

    def __str__(self):
        return f'{self.user}, {self.excel_file}'

    def save(self, *args, **kwargs):
        self.file_name = self.excel_file.name
        super(ExcelFile, self).save(*args, **kwargs)


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    excel_file = models.ForeignKey(ExcelFile, on_delete=models.CASCADE)
    tnved = models.CharField(max_length=64)
    full_product_name = models.CharField(max_length=128)
    trademark = models.CharField(max_length=64)
    article_type = models.CharField(max_length=64)
    article_value = models.CharField(max_length=64)
    product_type = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    target_gender = models.CharField(max_length=64)
    clothing_type = models.CharField(max_length=64)
    clothing_value = models.CharField(max_length=64)
    composition = models.CharField(max_length=64)
    standard_no = models.CharField(max_length=64)
    status = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.user}, {self.excel_file}'


class AddProductToExcelFile(models.Model):
    tnved = models.CharField(max_length=64)
    full_product_name = models.CharField(max_length=128)
    trademark = models.CharField(max_length=64)
    article_type = models.CharField(max_length=64)
    article_value = models.CharField(max_length=64)
    product_type = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    target_gender = models.CharField(max_length=64)
    clothing_type = models.CharField(max_length=64, default=0)
    clothing_value = models.CharField(max_length=64, default=0)
    composition = models.CharField(max_length=64)
    standard_no = models.CharField(max_length=64)
    status = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.full_product_name}"
