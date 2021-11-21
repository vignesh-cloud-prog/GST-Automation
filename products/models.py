from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model): 
    seller= models.ForeignKey(User, related_name="product", on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    desc= models.TextField(null=True,blank=True)
    selling_price=models.CharField(max_length=10)
    code= models.CharField(max_length=100,null=True,blank=True)
    gst_detail=models.TextField(null=True,blank=True)
    cgst= models.CharField(max_length=100,null=True,blank=True)
    sgst= models.CharField(max_length=100,null=True,blank=True)
    igst= models.CharField(max_length=100,null=True,blank=True)
    cess= models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return f"{self.seller} {self.name}"