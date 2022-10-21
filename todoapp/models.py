from django.db import models

# Create your models here.
class LotteryData(models.Model):
    filename = models.CharField(max_length=50, blank=True, null=True)
    lottery_name = models.CharField(max_length=50, blank=True, null=True)
    first_prize = models.CharField(max_length=100, blank=True, null=True)
    consolation_prize = models.CharField(max_length=250, blank=True, null=True)
    second_prize = models.TextField(blank=True, null=True)
    third_prize = models.TextField(blank=True, null=True)
    fourth_prize = models.TextField(blank=True, null=True)
    fifth_prize = models.TextField(blank=True, null=True)
    sixth_prize = models.TextField(blank=True, null=True)
    seventh_prize = models.TextField(blank=True, null=True)
    eighth_prize = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lottery_data'

class LotteryNew(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lottery_new'