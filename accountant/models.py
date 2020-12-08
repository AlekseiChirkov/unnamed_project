from django.db import models


class DailySalesReport(models.Model):
    product = models.CharField(max_length=255, db_index=True)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    total_sale = models.DecimalField(max_digits=15, decimal_places=2)
    orders = models.IntegerField()
    total_orders = models.IntegerField()

    def __str__(self):
        return self.product


class WeeklySalesReport(models.Model):
    product = models.CharField(max_length=255, db_index=True)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    total_sale = models.DecimalField(max_digits=15, decimal_places=2)
    orders = models.IntegerField()
    total_orders = models.IntegerField()

    def __str__(self):
        return self.product


class MonthlySalesReport(models.Model):
    product = models.CharField(max_length=255, db_index=True)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    total_sale = models.DecimalField(max_digits=15, decimal_places=2)
    orders = models.IntegerField()
    total_orders = models.IntegerField()

    def __str__(self):
        return self.product
