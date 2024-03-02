from django.shortcuts import render,redirect
from Admin.models import *
from Officer.models import *
from Guest.models import *
from Owner.models import *
from User.models import *

# Create your views here.

def officerhome(request):
    regdata=tbl_officer.objects.get(id=request.session['oid'])
    return render(request,"Officer/OfficerHomepage.html",{'regdata':regdata})

def myprofile(request):
    oregdata=tbl_officer.objects.get(id=request.session['oid'])
    return render(request,"Officer/MyProfile.html",{'oregdata':oregdata})


def editprofile(request):
    oregdata=tbl_officer.objects.get(id=request.session['oid'])
    if request.method=="POST":
        oregdata.name=request.POST.get("txt_name")
        oregdata.contact=request.POST.get("txt_con")
        oregdata.email=request.POST.get("txt_email")
        oregdata.address=request.POST.get("txt_address")
        oregdata.save()
        return redirect("Officer:MyProfile")
    else:
        return render(request,"Officer/EditProfile.html",{'oregdata':oregdata})       


def changepassword(request):
    oregdata=tbl_officer.objects.get(id=request.session['oid'])
    if request.method=="POST":
        pwd=oregdata.password
        current_pwd=request.POST.get("txt_pass")
        if pwd == current_pwd:
            pass1 = request.POST.get("txt_new")
            pass2 = request.POST.get("txt_cpass")
            if pass1==pass2 :
                oregdata.password=pass1
                oregdata.save()
                return redirect("Officer:ChangePassword")
            else:
                msg= "Password donot match"
                return render(request,"Officer/ChangePassword.html",{'msg':msg})
        else:
            msg="Incorrect password"
            return render(request,"Officer/ChangePassword.html",{'msg':msg})
    else:
        msg="Password changed"
        return render(request,"Officer/ChangePassword.html")

def ownerlist(request):
    owndata=tbl_ownerregistration.objects.filter(status=0)
    return render(request,"Officer/ViewOwnerList.html",{'owndata':owndata})       

def acceptedownerlist(request):
    owndata=tbl_ownerregistration.objects.filter(status=1)
    return render(request,"Officer/AcceptedOwnerList.html",{'owndata':owndata})       

def rejectedownerlist(request):
    owndata=tbl_ownerregistration.objects.filter(status=2)
    return render(request,"Officer/RejectedOwnerList.html",{'owndata':owndata})   


def acceptowner(request,aid):
    owndata=tbl_ownerregistration.objects.get(id=aid)
    owndata.status=1
    owndata.save()
    return redirect("Officer:ViewOwnerList")

def rejectowner(request,rid):
    owndata=tbl_ownerregistration.objects.get(id=rid)
    owndata.status=2
    owndata.save()
    return redirect("Officer:ViewOwnerList")    


def viewrent(request):
    countrydata=tbl_country.objects.get(id=request.session["codata"])
    rdata=tbl_rent.objects.filter(status=0,owner__place__district__state__country=countrydata)
    return render(request,"Officer/ViewRent.html",{'rdata':rdata})       
        

def rejectedrent(request):
    countrydata=tbl_country.objects.get(id=request.session["codata"])
    rdata=tbl_rent.objects.filter(status=2,owner__place__district__state__country=countrydata)
    return render(request,"Officer/RejectedRent.html",{'rdata':rdata})  

def acceptedrent(request):
    countrydata=tbl_country.objects.get(id=request.session["codata"])
    rdata=tbl_rent.objects.filter(status=1,owner__place__district__state__country=countrydata)
    return render(request,"Officer/AcceptedRent.html",{'rdata':rdata})  
         
def rejectrent(request,rid):
    data=tbl_rent.objects.get(id=rid)
    data.status=2
    data.save()
    return redirect("Officer:ViewRent")

def acceptrent(request,aid):
    data=tbl_rent.objects.get(id=aid)
    data.status=1
    data.save()
    return redirect("Officer:ViewRent")


def viewcomplaint(request):
    countrydata=tbl_country.objects.get(id=request.session["codata"])
    owndata=tbl_ownercomplaint.objects.filter(owner__place__district__state__country=countrydata)
    return render(request,"Officer/ViewComplaint.html",{'owndata':owndata}) 


def viewfeedback(request):
    countrydata=tbl_country.objects.get(id=request.session["codata"])
    udata=tbl_userfeedback.objects.filter(user__place__district__state__country=countrydata)
    return render(request,"Officer/ViewFeedback.html",{'udata':udata}) 