from django.db import models

# Create your models here.



class product_details(models.Model):
    product=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    sub_category=models.CharField(max_length=50)