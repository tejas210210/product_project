from django.db import models


class Product(models.Model):
    """This is product model"""
    name = models.CharField(max_length=30)
    description = models.TextField()
    cost_per_item = models.FloatField(default=0, null=True, blank=True)
    stock_quantity = models.IntegerField(default=0, null=True, blank=True)
    volume = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = "Product_Info"

    def save(self, *args, **kwargs):
        self.volume = self.cost_per_item * self.stock_quantity
        super(Product, self).save(*args, **kwargs)