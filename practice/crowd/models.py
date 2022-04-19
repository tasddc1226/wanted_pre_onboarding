from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    description = models.TextField()
    target_price = models.IntegerField()
    expiry_date = models.DateTimeField()
    funding_cost = models.IntegerField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:10]