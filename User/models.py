from django.db import models
from Guest.models import *
from Owner.models import *
from .models import *
# Create your models here.

class tbl_userrequest(models.Model):   
    # date=models.DateField(auto_now_add=True)  
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


class tbl_usercomplaint(models.Model):  
    complainttitle=models.CharField(max_length=50)
    complainttype=models.ForeignKey(tbl_complainttype,on_delete=models.CASCADE) 
    content=models.CharField(max_length=50)
    complaintdate=models.DateField(auto_now_add=True) 
    user=models.ForeignKey(tbl_userregistration,on_delete=models.SET_NULL,null=True)  

   

class tbl_userrating(models.Model): 
    rating_data=models.IntegerField()
    user_name=models.CharField(max_length=50)
    user_review=models.CharField(max_length=50)
    datetime=models.DateField(auto_now_add=True) 
    rent=models.ForeignKey(tbl_rent,on_delete=models.CASCADE)


class tbl_userfeedback(models.Model):  
    feedback=models.CharField(max_length=50)
    feedbackdate=models.DateField(auto_now_add=True) 
    user=models.ForeignKey(tbl_userregistration,on_delete=models.SET_NULL,null=True) 