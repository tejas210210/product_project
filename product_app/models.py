from django.db import models
from django.contrib.auth.models import User


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


class Token(models.Model):
    """The Token Model is define"""
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_token = models.CharField( max_length=200, null=False)

    class Meta:
        db_table = "Token_Info"

    def __str__(self):
        return self.user_token