from django.db import models

# Create your models here.


class rent(models.Model):
    bike_name=models.CharField(max_length=100,primary_key=True)   
    customer_name=models.CharField(max_length=100)
    bike_rent=models.BigIntegerField()
    def __str__(self):
        return self.bike_name

