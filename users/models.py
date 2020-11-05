from django.db import models
from admin1.models import*
# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    qty = models.IntegerField()
    priceUnit = models.FloatField()
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    dateOrder = models.DateTimeField()
    deliverDate = models.DateTimeField(null=True)
    status = models.IntegerField()
    
    @property
    def priceSum(self):
        return int(self.priceUnit*self.qty)
        
    class Status:
        PENDING = 0
        DELIVERED = 1
        CANCELED = 2