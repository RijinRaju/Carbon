from Users.models import User
from django.db import models

# Create your models here.


class Emission(models.Model):
    transportation = models.IntegerField(null=True)
    energyConsumption = models.IntegerField(null=True)
    foodConsumption = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    date  = models.DateField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    target = models.IntegerField(null=True)


