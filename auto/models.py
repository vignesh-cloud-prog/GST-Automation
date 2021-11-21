from django.db import models

# Create your models here.
class GST_Table(models.Model):
    hsn= models.CharField(max_length=100)
    desc= models.TextField()
    cgst= models.CharField(max_length=100)
    sgst= models.CharField(max_length=100)
    igst= models.CharField(max_length=100)
    cess= models.CharField(max_length=100)

    def __str__(self):
        return self.hsn+" "+self.desc