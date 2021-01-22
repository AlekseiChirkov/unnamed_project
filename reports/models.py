<<<<<<< HEAD
import pandas as pd

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from unnamed_project import settings

=======
from django.db import models
>>>>>>> e8c7acc5d40449e929e78e32019c72921639da13
from users.models import User


class ExcelFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    excel_file = models.FileField(upload_to='excel_files')

    def __str__(self):
        return f'{self.user}, {self.excel_file}'

@receiver(post_save, sender=ExcelFile)
def save_file_data(sender, instance, created, **kwargs):
    if created:
        file = instance
        excel_file = file.excel_file.url
        file_dir = settings.BASE_DIR + excel_file
        data = pd.read_excel(file_dir, skiprows=3)
        df = pd.DataFrame(data)
        df = df.dropna(how='all')
        df_list = df.values.tolist()
        rows = [[str(j) for j in i] for i in df_list]
        cleaned_rows = [i for i in rows if i]
        print(cleaned_rows)
        for i in cleaned_rows:
            print(i[0])
            article = Article.objects.create(
                article_type=str(i[3]),
                article_value=str(i[4])
            )
            article.save()
            clothing_size = ClothingSize.objects.create(
                clothing_type=str(i[8]),
                clothing_value=str(i[9])
            )
            clothing_size.save()
            report = Report.objects.create(
                user=instance.user,
                excel_file=instance,
                tnved=str(i[0]),
                full_product_name=str(i[1]),
                trademark=str(i[2]),
                article=article,
                product_type=str(i[5]),
                color=str(i[6]),
                target_gender=str(i[7]),
                clothing_size=clothing_size,
                composition=str(i[10]),
                standard_no=str(i[11]),
                status=str(i[12])
            )
            report.save()
=======
    excel_file = models.FileField()

    # def __str__(self):
    #     return '%s %s' % (self.user, self.excel_file)
>>>>>>> e8c7acc5d40449e929e78e32019c72921639da13


class Article(models.Model):
    article_type = models.CharField(max_length=64)
    article_value = models.CharField(max_length=64)

<<<<<<< HEAD
    def __str__(self):
        return f'{self.article_type}, {self.article_value}'
=======
    # def __str__(self):
    #     return str(self.article_type), str(self.article_value)
>>>>>>> e8c7acc5d40449e929e78e32019c72921639da13


class ClothingSize(models.Model):
    clothing_type = models.CharField(max_length=64)
    clothing_value = models.CharField(max_length=64)

<<<<<<< HEAD
    def __str__(self):
        return f'{self.clothing_type}, {self.clothing_value}'
=======
    # def __str__(self):
    #     return str(self.clothing_type), str(self.clothing_value)
>>>>>>> e8c7acc5d40449e929e78e32019c72921639da13


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    excel_file = models.ForeignKey(ExcelFile, on_delete=models.CASCADE)
=======
>>>>>>> e8c7acc5d40449e929e78e32019c72921639da13
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

<<<<<<< HEAD
    def __str__(self):
        return f'{self.user}, {self.excel_file}'
=======
    # def __str__(self):
    #     return '%s %s %s %s %s %s %s %s %s %s %s %s' % (
    #         self.user, self.tnved, self.full_product_name, self.trademark, self.article,
    #         self.product_type, self.color, self.target_gender, self.clothing_size,
    #         self.composition, self.standard_no, self.status
    #     )
>>>>>>> e8c7acc5d40449e929e78e32019c72921639da13

