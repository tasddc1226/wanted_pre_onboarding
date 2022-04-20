import datetime
from django.db import models

# Create your models here.
class Product(models.Model):
    # 상품 title
    title = models.CharField(max_length=100)
    # 작성자
    writer = models.CharField(max_length=100, null=False)
    # 상품 설명
    description = models.TextField()
    # 목표 펀딩 가격
    target_price = models.IntegerField(null=False, blank=False)
    # 만료 기간
    expiry_date = models.DateField(null=False, blank=False)
    # 1회 펀딩 비용
    funding_cost = models.IntegerField(null=False, blank=False)
    # 총 펀딩 금액
    total_cost = models.IntegerField(default=0)
    # 참여자 수
    participants = models.IntegerField(default=0)
    # 생성일
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:10]
    
    def getAchievement_rate(self):
        return f'{(self.total_cost / self.target_price) * 100 :.0f}%'
    
    def getD_day(self):
        now = datetime.date.today()
        tmp = list(map(int, str(self.expiry_date).split('-')))
        target = datetime.date(tmp[0], tmp[1], tmp[2])
        return (target - now).days

    def setParticipants(self):
        self.participants += 1
    
    def getParticipants(self):
        return self.participants