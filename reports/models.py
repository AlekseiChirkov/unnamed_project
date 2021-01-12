from django.db import models
from users.models import User


class ExcelFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    excel_file = models.FileField()

    # def __str__(self):
    #     return '%s %s' % (self.user, self.excel_file)


class Article(models.Model):
    article_type = models.CharField(max_length=64)
    article_value = models.CharField(max_length=64)

    # def __str__(self):
    #     return str(self.article_type), str(self.article_value)


class ClothingSize(models.Model):
    clothing_type = models.CharField(max_length=64)
    clothing_value = models.CharField(max_length=64)

    # def __str__(self):
    #     return str(self.clothing_type), str(self.clothing_value)


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tnved = models.CharField(max_length=64)
    full_product_name = models.CharField(max_length=128)
    trademark = models.CharField(max_length=64)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    target_gender = models.CharField(max_length=64)
    clothing_size = models.ForeignKey(ClothingSize, on_delete=models.CASCADE)
    composition = models.CharField(max_length=64)
    standard_no = models.CharField(max_length=64)
    status = models.CharField(max_length=64)

    # def __str__(self):
    #     return '%s %s %s %s %s %s %s %s %s %s %s %s' % (
    #         self.user, self.tnved, self.full_product_name, self.trademark, self.article,
    #         self.product_type, self.color, self.target_gender, self.clothing_size,
    #         self.composition, self.standard_no, self.status
    #     )

