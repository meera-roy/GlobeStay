from django.db import models
from Admin.models import *
from Guest.models import tbl_ownerregistration

# Create your models here.

class tbl_rent(models.Model): 
    renttype=models.ForeignKey(tbl_renttype,on_delete=models.CASCADE)    
    name=models.CharField(max_length=50)  
    image=models.FileField(upload_to="MemberDocs/") 
    amount=models.IntegerField() 
    details=models.CharField(max_length=50)
    owner=models.ForeignKey(tbl_ownerregistration,on_delete=models.CASCADE)  
    status=models.IntegerField(default=0)

class tbl_rentgallery(models.Model):  
    galleryimage=models.FileField(upload_to="MemberDocs/")  
    rent=models.ForeignKey(tbl_rent,on_delete=models.CASCADE) 
     