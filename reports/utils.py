import pandas as pd
<<<<<<< HEAD
import excel2json

from reports.models import Report, Article, ClothingSize, ExcelFile
from users.models import User


# def excel_data_in_model(request):
#     file_obj = request.FILES['excel_file'].file
#     data = pd.read_excel(file_obj, skiprows=3)
#     df = pd.DataFrame(data)
#     df = df.dropna(how='all')
#     df_list = df.values.tolist()
#     rows = [[str(j) for j in i] for i in df_list]
#     cleaned_rows = [i for i in rows if i]
#     print(cleaned_rows)
#     for i in cleaned_rows:
#         print(i[0])
#         article = Article.objects.create(
#             article_type=str(i[3]),
#             article_value=str(i[4])
#         )
#         article.save()
#         clothing_size = ClothingSize.objects.create(
#             clothing_type=str(i[8]),
#             clothing_value=str(i[9])
#         )
#         clothing_size.save()
#         report = Report.objects.create(
#             user=User.objects.get(id=1),
#             tnved=str(i[0]),
#             full_product_name=str(i[1]),
#             trademark=str(i[2]),
#             article=article,
#             product_type=str(i[5]),
#             color=str(i[6]),
#             target_gender=str(i[7]),
#             clothing_size=clothing_size,
#             composition=str(i[10]),
#             standard_no=str(i[11]),
#             status=str(i[12])
#         )
#         report.save()
=======

from .models import Report, Article, ClothingSize


def excel_data_in_model(request):
    file_obj = request.FILES['excel_file'].file
    data = pd.read_excel(file_obj)
    df = pd.DataFrame(data, columns=[
        'Код ТНВЭД', 'Полное наименование товара', 'Товарный знак', 'Модель / артикул производителя',
        'Вид товара', 'Цвет', 'Целевой пол', 'Размер одежды', 'Состав', 'Номер Регламента/стандарта',
        'Статус карточки товара в Каталоге', 'Статус карточки товара в Каталоге'
    ])
    df_list = df.values.tolist()
    df_list = [[str(j) for j in i] for i in df_list]
    rows = [[j for j in i if j != 'nan'] for i in df_list]
    cleaned_rows = [i for i in rows if i]
    for i in cleaned_rows:
        article = Article.objects.create(
            article_type=str(i[3]),
            article_value=str(i[3])
        )
        article.save()
        clothing_size = ClothingSize.objects.create(
            clothing_type=str(i[7]),
            clothing_value=str(i[7])
        )
        clothing_size.save()
        report = Report.objects.create(
            user=request.user,
            tnved=str(i[0]),
            full_product_name=str(i[1]),
            trademark=str(i[2]),
            article=article,
            product_type=str(i[4]),
            color=str(i[5]),
            target_gender=str(i[6]),
            clothing_size=clothing_size,
            composition=str(i[8]),
            standard_no=str(i[9]),
            status=str(i[10])
        )
        report.save()
>>>>>>> e8c7acc5d40449e929e78e32019c72921639da13
