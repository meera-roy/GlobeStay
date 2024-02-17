from django.db import models
from Admin.models import tbl_place

# Create your models here.
class tbl_ownerregistration(models.Model): 
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)    
    name=models.CharField(max_length=50)  
    contact=models.CharField(max_length=50) 
    email=models.EmailField(max_length=50)
    gender=models.CharField(max_length=50) 
    address=models.TextField(max_length=50) 
    zipcode=models.CharField(max_length=50)
    photo=models.FileField(upload_to="MemberDocs/")  
    proof=models.FileField(upload_to="MemberDocs/") 
    password=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default=0,null=True)


   
class tbl_userregistration(models.Model): 
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)    
    name=models.CharField(max_length=50)  
    contact=models.CharField(max_length=50) 
    email=models.EmailField(max_length=50)
    gender=models.CharField(max_length=50) 
    address=models.TextField(max_length=50) 
    zipcode=models.CharField(max_length=50)
    photo=models.FileField(upload_to="MemberDocs/")  
    proof=models.FileField(upload_to="MemberDocs/") 
    password=models.CharField(max_length=50) 