from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Owner.models import *
from User.models import *

# Create your views here.
def ownerhome(request):
    oregdata=tbl_ownerregistration.objects.get(id=request.session['oid'])
    return render(request,"Owner/OwnerHomepage.html",{'oregdata':oregdata})

def myprofile(request):
    oregdata=tbl_ownerregistration.objects.get(id=request.session['oid'])
    return render(request,"Owner/MyProfile.html",{'oregdata':oregdata})

def editprofile(request):
    oregdata=tbl_ownerregistration.objects.get(id=request.session['oid'])
    if request.method=="POST":
        oregdata.name=request.POST.get("txt_name")
        oregdata.contact=request.POST.get("txt_con")
        oregdata.email=request.POST.get("txt_email")
        oregdata.address=request.POST.get("txt_address")
        oregdata.save()
        return redirect("Owner:MyProfile")
    else:
        return render(request,"Owner/EditProfile.html",{'oregdata':oregdata})        

def changepassword(request):
    oregdata=tbl_ownerregistration.objects.get(id=request.session['oid'])
    if request.method=="POST":
        pwd=oregdata.password
        current_pwd=request.POST.get("txt_pass")
        if pwd == current_pwd:
            pass1 = request.POST.get("txt_new")
            pass2 = request.POST.get("txt_cpass")
            if pass1==pass2 :
                oregdata.password=pass1
                oregdata.save()
                return redirect("Owner:ChangePassword")
            else:
                msg= "Password donot match"
                return render(request,"Owner/ChangePassword.html",{'msg':msg})
        else:
            msg="Incorrect password"
            return render(request,"Owner/ChangePassword.html",{'msg':msg})
    else:
        msg="Password changed"
        return render(request,"Owner/ChangePassword.html")


def rent(request):
    ownerdata=tbl_ownerregistration.objects.get(id=request.session['oid'])
    rentid=tbl_renttype.objects.all()
    rent=tbl_rent.objects.filter(owner=ownerdata)
    if request.method=="POST" and request.FILES:
        renttypedata=tbl_renttype.objects.get(id=request.POST.get('select_ren'))
        tbl_rent.objects.create(
        name = request.POST.get("txt_name"),
        image = request.FILES.get("txt_img"),
        amount = request.POST.get("txt_amount"),
        details = request.POST.get("txt_det"),
        renttype = renttypedata,
        owner=ownerdata
        )
        return render(request,"Owner/Rent.html",{'rentid':rentid,'rent':rent})
    else:
        return render(request,"Owner/Rent.html",{'rentid':rentid,'rent':rent})    

def DeleteRent(request,did):
    tbl_rent.objects.get(id=did).delete()
    return redirect("Owner:Rent")            
        
def rentgallery(request,rid):
    if request.method=="POST" and request.FILES:
        rentdata=tbl_rent.objects.get(id=rid)
        tbl_rentgallery.objects.create(galleryimage=request.FILES.get("txt_img"),rent=rentdata)
        return redirect("Owner:Rent") 
    else:
        return render(request,"Owner/Rentgallery.html")

def userbooking(request):
    oregdata=tbl_ownerregistration.objects.get(id=request.session['oid'])
    udata=tbl_userrequest.objects.filter(rent__owner=oregdata,status=0)
    
    return render(request,"Owner/UserBooking.html",{'udata':udata,'oregdata':oregdata})      

def accepteduserbooking(request):
    oregdata=tbl_ownerregistration.objects.get(id=request.session['oid'])
    udata=tbl_userrequest.objects.filter(rent__owner=oregdata,status=1)
    
    return render(request,"Owner/AcceptedUserBooking.html",{'udata':udata,'oregdata':oregdata})     


def rejecteduserbooking(request):
    oregdata=tbl_ownerregistration.objects.get(id=request.session['oid'])
    udata=tbl_userrequest.objects.filter(rent__owner=oregdata,status=2)
    
    return render(request,"Owner/RejectedUserBooking.html",{'udata':udata,'oregdata':oregdata})     

def acceptbook(request,aid):
    data=tbl_userrequest.objects.get(id=aid)
    data.status=1
    data.save()
    return redirect("Owner:UserBooking")

def rejectbook(request,rid):
    data=tbl_userrequest.objects.get(id=rid)
    data.status=2
    data.save()
    return redirect("Owner:UserBooking")


def complaint(request):
    oregdata=tbl_ownerregistration.objects.get(id=request.session['oid'])
    comdata=tbl_complainttype.objects.all()
    compdata=tbl_ownercomplaint.objects.all()
    if request.method=="POST":
        com=tbl_complainttype.objects.get(id=request.POST.get("select_com"))
        tbl_ownercomplaint.objects.create(
            
            complainttitle = request.POST.get("txt_name"),
            content = request.POST.get("txt_content"),
            complainttype=com,
            owner=oregdata,

        )
        return render(request,"Owner/OwnerComplaint.html",{'oregdata':oregdata,'comdata':comdata,'compdata':compdata}) 
    else:
        return render(request,"Owner/OwnerComplaint.html",{'oregdata':oregdata,'comdata':comdata,'compdata':compdata})     

def DeleteComplaint(request,did):
    tbl_ownercomplaint.objects.get(id=did).delete()
    return redirect("Owner:OwnerComplaint")    



def logout(request):
    del request.session["aid"]
    return redirect("Guest:Login")    