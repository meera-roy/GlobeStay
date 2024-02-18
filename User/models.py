from django.db import models
from Guest.models import *
from Owner.models import *
# Create your models here.

class tbl_userrequest(models.Model):   
    #date=models.DateField(auto_now_add=True)  
    file=models.FileField(upload_to="MemberDocs/") 
    content=models.CharField(max_length=50)
    fromdate=models.DateField()
    todate=models.DateField()
    user=models.ForeignKey(tbl_userregistration,on_delete=models.CASCADE)  
    rent=models.ForeignKey(tbl_rent,on_delete=models.CASCADE) 
    status=models.CharField(max_length=50,default=0)


class tbl_book(models.Model):   
    file=models.FileField(upload_to="MemberDocs/")   
    content=models.CharField(max_length=50)   