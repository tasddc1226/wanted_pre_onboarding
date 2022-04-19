from django.db import models

# Create your models here.
class Product(models.Model):
    # 상품 id
    id = models.AutoField(primary_key=True, null=False, blank=False)
    # 상품 title
    title = models.CharField(max_length=100)
    # 작성자
    writer = models.CharField(max_length=100, null=False)
    # 상품 설명
    description = models.TextField()
    # 목표 펀딩 가격
    target_price = models.CharField(max_length=100)
    # 만료 기간
    expiry_date = models.DateTimeField()
    # 1회 펀딩 비용
    funding_cost = models.CharField(max_length=100)
    # 총 펀딩 금액
    total_cost = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:10]