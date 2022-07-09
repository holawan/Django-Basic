from django.db import models

# Create your models here.

from django.contrib.auth.models import User as U
from django.contrib.auth.models import AbstractUser

class PayPlan(models.Model) :
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

#AbstractUser 상속받기 
class Users(AbstractUser) :
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)

#장고 내부 USER 모델에과 onetoeone 관계만들어서 detail 관리하기 
class UserDetail(models.Model) :
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    pay_plan = models.ForeignKey(PayPlan,on_delete=models.DO_NOTHING)