from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class GST(models.Model):
    user = models.OneToOneField(User, related_name="gst", on_delete=models.CASCADE)
    hsn= models.CharField(max_length=100)
    desc= models.TextField()
    cgst= models.CharField(max_length=100,null=True,blank=True)
    sgst= models.CharField(max_length=100,null=True,blank=True)
    igst= models.CharField(max_length=100,null=True,blank=True)
    cess= models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return f"{self.user} {self.hsn}"
