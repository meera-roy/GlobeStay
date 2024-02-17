from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Owner.models import *
from User.models import *
import random
# Create your views here.
def userhome(request):
    uregdata=tbl_userregistration.objects.get(id=request.session['uid'])
    return render(request,"User/UserHomePage.html",{'uregdata':uregdata})

def myprofile(request):
    uregdata=tbl_userregistration.objects.get(id=request.session['uid'])
    return render(request,"User/MyProfile.html",{'uregdata':uregdata})
    
def editprofile(request):
    uregdata=tbl_userregistration.objects.get(id=request.session['uid'])
    if request.method=="POST":
        uregdata.name=request.POST.get("txt_name")
        uregdata.contact=request.POST.get("txt_con")
        uregdata.email=request.POST.get("txt_email")
        uregdata.address=request.POST.get("txt_address")
        uregdata.save()
        return redirect("User:MyProfile")
    else:
        return render(request,"User/EditProfile.html",{'uregdata':uregdata}) 

def changepassword(request):
    uregdata=tbl_userregistration.objects.get(id=request.session['uid'])
    if request.method=="POST":
        pwd=uregdata.password
        current_pwd=request.POST.get("txt_pass")
        if pwd == current_pwd:
            pass1 = request.POST.get("txt_new")
            pass2 = request.POST.get("txt_cpass")
            if pass1==pass2 :
                uregdata.password=pass1
                uregdata.save()
                return redirect("User:ChangePassword")
            else:
                msg= "Password donot match"
                return render(request,"User/ChangePassword.html",{'msg':msg})
        else:
            msg="Incorrect password"
            return render(request,"User/ChangePassword.html",{'msg':msg})
    else:
        msg="Password changed"
        return render(request,"User/ChangePassword.html",)

def viewrents(request):
    coudata=tbl_country.objects.all()
    stdata=tbl_state.objects.all()
    disdata=tbl_district.objects.all()
    pladata=tbl_place.objects.all()
    rent=tbl_rent.objects.all()
    renttype=tbl_renttype.objects.all()
    if request.method=="POST":
        return render(request,"User/ViewRents.html",{'rent':rent,'coudata':coudata,'stdata':stdata,'disdata':disdata,'pladata':pladata,'renttype':renttype})
    else:
        return render(request,"User/ViewRents.html",{'rent':rent,'coudata':coudata,'stdata':stdata,'disdata':disdata,'pladata':pladata,'renttype':renttype})

def ajaxrent(request):
    if request.GET.get('rid')!="":
        renttypedata=tbl_renttype.objects.get(id=request.GET.get('rid'))
        if request.GET.get('pid')!="":
            placedata=tbl_place.objects.get(id=request.GET.get('pid'))
            rentdata=tbl_rent.objects.filter(owner__place=placedata,renttype=renttypedata)
            return render(request,"User/ajaxrent.html",{'data':rentdata})
        elif request.GET.get('did')!="":
            districtdata=tbl_district.objects.get(id=request.GET.get('did'))
            rentdata=tbl_rent.objects.filter(owner__place__district=districtdata,renttype=renttypedata)
            return render(request,"User/ajaxrent.html",{'data':rentdata})
        elif request.GET.get('sid')!="":
            statedata=tbl_state.objects.get(id=request.GET.get('sid'))
            rentdata=tbl_rent.objects.filter(owner__place__district__state=statedata,renttype=renttypedata)
            return render(request,"User/ajaxrent.html",{'data':rentdata})    
        elif request.GET.get('cid')!="":
            countrydata=tbl_country.objects.get(id=request.GET.get('cid'))
            rentdata=tbl_rent.objects.filter(owner__place__district__state__country=countrydata,renttype=renttypedata)
            return render(request,"User/ajaxrent.html",{'data':rentdata})
        else:
            rentdata=tbl_rent.objects.filter(renttype=renttypedata)
            return render(request,"User/ajaxrent.html",{'data':rentdata})
    else:
        if request.GET.get('pid')!="":
            placedata=tbl_place.objects.get(id=request.GET.get('pid'))
            rentdata=tbl_rent.objects.filter(owner__place=placedata)
            return render(request,"User/ajaxrent.html",{'data':rentdata})
        elif request.GET.get('did')!="":
            districtdata=tbl_district.objects.get(id=request.GET.get('did'))
            rentdata=tbl_rent.objects.filter(owner__place__district=districtdata)
            return render(request,"User/ajaxrent.html",{'data':rentdata})
        elif request.GET.get('sid')!="":
            statedata=tbl_state.objects.get(id=request.GET.get('sid'))
            rentdata=tbl_rent.objects.filter(owner__place__district__state=statedata)
            return render(request,"User/ajaxrent.html",{'data':rentdata})    
        else:
            countrydata=tbl_country.objects.get(id=request.GET.get('cid'))
            rentdata=tbl_rent.objects.filter(owner__place__district__state__country=countrydata)
            return render(request,"User/ajaxrent.html",{'data':rentdata})


def complaint(request):
    uregdata=tbl_userregistration.objects.get(id=request.session['uid'])
    return render(request,"User/Complaint.html",{'uregdata':uregdata}) 

def feedback(request):
    uregdata=tbl_userregistration.objects.get(id=request.session['uid'])
    return render(request,"User/Feedback.html",{'uregdata':uregdata})    


def book(request):
    uregdata=tbl_userregistration.objects.get(id=request.session['uid'])
    return render(request,"User/Book.html",{'uregdata':uregdata})      


def userrequest(request,rid):
    uregdata=tbl_userregistration.objects.get(id=request.session['uid'])
    rentdata=tbl_rent.objects.get(id=rid)
    if request.method=="POST":

        tbl_userrequest.objects.create(
            file = request.FILES.get("txt_file"),
            content = request.POST.get("txt_content"),
            user=uregdata,
            rent=rentdata,

        )  
        return render(request,"User/UserRequest.html",{'uregdata':uregdata,'rentdata':rentdata})    
    else:
        return render(request,"User/UserRequest.html",{'uregdata':uregdata,'rentdata':rentdata})              


def mybooking(request):
    uregdata=tbl_userregistration.objects.get(id=request.session['uid'])
    udata=tbl_userrequest.objects.filter(user=uregdata)
    return render(request,"User/MyBooking.html",{'udata':udata,'uregdata':uregdata})     


def advancepayment(request,rid):
    rentdata=tbl_rent.objects.get(id=rid)
    userdata=tbl_userregistration.objects.get(id=request.session["uid"])
    amount=int(rentdata.amount)
    advance=amount*.25
    receiptnumber=random.randint(111111,999999) 
    if request.method=="POST":
        urdata=tbl_userrequest.objects.get(user=userdata,rent=rentdata,status=1)
        urdata.status=3
        urdata.save()

        return redirect("User:Loader")
    else:
        return render(request,"User/AdvancePayment.html",{'receipt':receiptnumber,'advance':advance})


def loader(request):
    return render(request,"User/Loader.html")



def success(request):
    return render(request,"User/Success.html")
