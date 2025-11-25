from django.db import models
from django.contrib import admin
class product(models.Model):
    product_id=models.CharField(primary_key=True,max_length=8)
    name=models.CharField(max_length=10)
    price=models.CharField(max_length=10)
    description=models.CharField(max_length=30)
    mfc_date=models.CharField(max_length=10)
    seller_id=models.CharField(max_length=10)
    brand=models.CharField(max_length=10)
    
class productAdmin(admin.ModelAdmin):
    list_display=["product_id","name","price","description","mfc_date","seller_id","brand"]
    
    
    
