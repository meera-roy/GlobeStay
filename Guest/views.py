from django.shortcuts import render,redirect
from .models import*
from Admin.models import*

# Create your views here.
def oreg(request):
    coudata=tbl_country.objects.all()
    oregdata=tbl_ownerregistration.objects.all()
    if request.method=="POST":
        placedata=tbl_place.objects.get(id=request.POST.get('select_pla'))
        tbl_ownerregistration.objects.create(photo=request.FILES.get('txt_photo'),
        proof=request.FILES.get('txt_proof'),place=placedata,name=request.POST.get("txt_name"),contact=request.POST.get("txt_contact"),email=request.POST.get("txt_email"),
        gender=request.POST.get("btn_gen"),address=request.POST.get("txt_add"),password=request.POST.get("txt_pass"),zipcode=request.POST.get("txt_zipcode"))
        return render(request,"Guest/OwnerRegistration.html",{'ownerregistration':oregdata,'coudata':coudata})
    else:
        return render(request,"Guest/OwnerRegistration.html",{'ownerregistration':oregdata,'coudata':coudata})

def ajaxplace(request):
    
    dis=tbl_district.objects.get(id=request.GET.get('district'))
    pla=tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{'pla':pla})   



def ureg(request):
    coudata=tbl_country.objects.all()
    uregdata=tbl_userregistration.objects.all()
    if request.method=="POST":
        placedata=tbl_place.objects.get(id=request.POST.get('select_pla'))
        tbl_userregistration.objects.create(photo=request.FILES.get('txt_photo'),
        proof=request.FILES.get('txt_proof'),place=placedata,name=request.POST.get("txt_name"),contact=request.POST.get("txt_contact"),email=request.POST.get("txt_email"),
        gender=request.POST.get("btn_gen"),address=request.POST.get("txt_add"),password=request.POST.get("txt_pass"),zipcode=request.POST.get("txt_zipcode"))
        return render(request,"Guest/UserRegistration.html",{'userregistration':uregdata,'coudata':coudata})
    else:
        return render(request,"Guest/UserRegistration.html",{'userregistration':uregdata,'coudata':coudata})


def ajaxplace(request):
    
    dis=tbl_district.objects.get(id=request.GET.get('district'))
    pla=tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{'pla':pla})   


def login(request):
    if request.method=="POST":
        Email=request.POST.get('txt_email')
        Password=request.POST.get('txt_pass')

        ucount=tbl_userregistration.objects.filter(email=Email,password=Password).count()
        ocount=tbl_ownerregistration.objects.filter(email=Email,password=Password,status=3).count()
        acount=tbl_adminlogin.objects.filter(email=Email,password=Password).count()
        ofcount=tbl_officer.objects.filter(email=Email,password=Password).count()
        if ucount > 0:
            uregdata=tbl_userregistration.objects.get(email=Email,password=Password)
            request.session['uid']=uregdata.id
            return redirect('User:UserHome')  
        elif ocount > 0:
            oregdata=tbl_ownerregistration.objects.get(email=Email,password=Password)
            request.session['oid']=oregdata.id
            return redirect('Owner:OwnerHome')
        elif acount > 0:
            adata=tbl_adminlogin.objects.get(email=Email,password=Password)
            request.session['aid']=adata.id
            return redirect('Admin:homepage')    
        elif ofcount > 0:
            regdata=tbl_officer.objects.get(email=Email,password=Password)
            request.session['oid']=regdata.id
            request.session["codata"]=regdata.country.id
            return redirect('Officer:OfficerHome')     
        
        else:
            msg = "Invalid Credentials!!"
            return render(request,"Guest/Login.html",{'msg':msg})
    else:
        return render(request,"Guest/Login.html")

def index(request):
    return render(request,"Guest/index.html")
