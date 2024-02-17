from django.db import models

# Create your models here.

class tbl_country(models.Model):
    country_name=models.CharField(max_length=50)

class tbl_renttype(models.Model):
    renttype_name=models.CharField(max_length=50)

class tbl_state(models.Model):
    state_name=models.CharField(max_length=50)  
    country=models.ForeignKey(tbl_country,on_delete=models.CASCADE)
  
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)  
    country=models.ForeignKey(tbl_country,on_delete=models.CASCADE)  
    state=models.ForeignKey(tbl_state,on_delete=models.CASCADE)  

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)  
    country=models.ForeignKey(tbl_country,on_delete=models.CASCADE)  
    state=models.ForeignKey(tbl_state,on_delete=models.CASCADE)    
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)      

class tbl_officer(models.Model): 
    country=models.ForeignKey(tbl_country,on_delete=models.CASCADE)    
    name=models.CharField(max_length=50)  
    contact=models.IntegerField(max_length=50) 
    email=models.EmailField(max_length=50)  
    address=models.TextField(max_length=50) 
    photo=models.FileField(upload_to="MemberDocs/")  
    password=models.CharField(max_length=50)  
    
class tbl_complainttype(models.Model):
    complaint_name=models.CharField(max_length=50)  



