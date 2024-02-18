from django.shortcuts import render,redirect
from .models import*
from Guest.models import *

# Create your views here.

def cou(request):
    coudata=tbl_country.objects.all()
    if request.method=="POST":
        datacount=tbl_country.objects.filter(country_name=request.POST.get("txt_country")).count()
        if datacount>0:
            return render(request,"Admin/Country.html",{'country':coudata})
            tbl_country.objects.create(country_name=request.POST.get("txt_country"))
        else:
            tbl_country.objects.create(country_name=request.POST.get("txt_country"))        
            return render(request,"Admin/Country.html",{'country':coudata})
    else:
        return render(request,"Admin/Country.html",{'country':coudata})

def DeleteCountry(request,did):
    tbl_country.objects.get(id=did).delete()
    return redirect("Admin:Country")

def EditCountry(request,eid):
    cou=tbl_country.objects.get(id=eid)
    coudata=tbl_country.objects.all()
    if request.method=="POST":
        cou.country_name=request.POST.get("txt_country")
        cou.save()
        return redirect("Admin:Country")
    else:
        return render(request,"Admin/Country.html",{'ecou':cou,'country':coudata})    
        
    



def ren(request):
    rendata=tbl_renttype.objects.all()
    if request.method=="POST":
        datacount=tbl_renttype.objects.filter(renttype_name=request.POST.grt("txt_renttype")).count()
        if datacount>0:
            return render(request,"Admin/RentType.html",{'renttype':rendata})
        else:    
            tbl_renttype.objects.create(renttype_name=request.POST.get("txt_renttype"))
            return render(request,"Admin/RentType.html",{'renttype':rendata})
    else:
        return render(request,"Admin/RentType.html",{'renttype':rendata})

def DeleteRentType(request,did):
    tbl_renttype.objects.get(id=did).delete()
    return redirect("Admin:RentType")          


def sta(request):
    coudata=tbl_country.objects.all()
    stadata=tbl_state.objects.all()
    if request.method=="POST":
        cou = tbl_country.objects.get(id=request.POST.get("select_cou"))
        datacount=tbl_state.objects.filter( state_name=request.POST.get("txt_state"),
            country=cou).count()

        if datacount>0:
            return render(request,"Admin/State.html",{'state':stadata,'coudata':coudata})
        else:
            tbl_state.objects.create(
            state_name=request.POST.get("txt_state"),
            country=cou
            )
            return render(request,"Admin/State.html",{'state':stadata,'coudata':coudata})
    else:
        return render(request,"Admin/State.html",{'state':stadata,'coudata':coudata})   

def DeleteState(request,did):
    tbl_state.objects.get(id=did).delete()
    return redirect("Admin:State")       


def dis(request):
    coudata=tbl_country.objects.all()
    stadata=tbl_state.objects.all()
    disdata=tbl_district.objects.all()
    if request.method=="POST":
        cou = tbl_country.objects.get(id=request.POST.get("select_cou"))
        sta = tbl_state.objects.get(id=request.POST.get("select_sta"))
        datacount=tbl_district.objects.filter(district_name=request.POST.get("txt_district"),
            country=cou,state=sta).count()
        if datacount>0:
            return render(request,"Admin/district.html",{'coudata':coudata,'disdata':disdata})
        else:    

            tbl_district.objects.create(
            district_name=request.POST.get("txt_district"),
            country=cou,
            state=sta
            )
            return render(request,"Admin/district.html",{'coudata':coudata,'disdata':disdata})
    else:
        return render(request,"Admin/district.html",{'coudata':coudata,'disdata':disdata})          

def ajaxstate(request):
    coun=tbl_country.objects.get(id=request.GET.get('country'))
    st=tbl_state.objects.filter(country=coun)
    return render(request,"Admin/AjaxState.html",{'st':st})

def DeleteDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:district")    


def pla(request):
    coudata=tbl_country.objects.all()
    stadata=tbl_state.objects.all()
    disdata=tbl_district.objects.all()
    pladata=tbl_place.objects.all()
    if request.method=="POST":
        cou = tbl_country.objects.get(id=request.POST.get("select_cou"))
        sta = tbl_state.objects.get(id=request.POST.get("select_sta"))
        dis = tbl_district.objects.get(id=request.POST.get("select_dis"))
        datacount=tbl_place.objects.filter(place_name=request.POST.get("txt_place"),
            country=cou,state=sta,district=dis).count()
        if datacount>0:
            return render(request,"Admin/place.html",{'coudata':coudata,'pladata':pladata})    

            tbl_place.objects.create( 
            place_name=request.POST.get("txt_place"),
            country=cou,
            state=sta,
            district=dis
            )
            return render(request,"Admin/place.html",{'coudata':coudata,'pladata':pladata})
    else:
        return render(request,"Admin/place.html",{'coudata':coudata,'pladata':pladata})       

def ajaxstate(request):
    coun=tbl_country.objects.get(id=request.GET.get('country'))
    st=tbl_state.objects.filter(country=coun)
    return render(request,"Admin/AjaxState.html",{'st':st})
def ajaxdistrict(request):
    
    st=tbl_state.objects.get(id=request.GET.get('state'))
    dis=tbl_district.objects.filter(state=st)
    return render(request,"Admin/AjaxDistrict.html",{'dis':dis})

def DeletePlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Admin:place")    

def reg(request):
    coudata=tbl_country.objects.all()
    regdata=tbl_officer.objects.all()
    if request.method=="POST":
        cou = tbl_country.objects.get(id=request.POST.get("select_cou"))
        tbl_officer.objects.create(
        name=request.POST.get("txt_name"),contact = request.POST.get("txt_contact"),
        email = request.POST.get("txt_email"),
        address = request.POST.get("txt_add"),
        country = cou,
        photo = request.FILES.get("txt_photo"),
        password = request.POST.get("txt_pass"))
            
        
        return render(request,"Admin/Officer.html",{'officer':regdata,'coudata':coudata})
    else:
        return render(request,"Admin/Officer.html",{'officer':regdata,'coudata':coudata})       

def ownerlist(request):
    owndata=tbl_ownerregistration.objects.filter(status=2)
    return render(request,"Admin/ViewOwnerList.html",{'owndata':owndata})       
        
def acceptedownerlist(request):
    owndata=tbl_ownerregistration.objects.filter(status=3)
    return render(request,"Admin/AcceptedOwnerList.html",{'owndata':owndata})       

def rejectedownerlist(request):
    owndata=tbl_ownerregistration.objects.filter(status=4)
    return render(request,"Admin/RejectedOwnerList.html",{'owndata':owndata})   

def acceptowner(request,aid):
    owndata=tbl_ownerregistration.objects.get(id=aid)
    owndata.status=3
    owndata.save()
    return redirect("Admin:ViewOwnerList")

def rejectowner(request,rid):
    owndata=tbl_ownerregistration.objects.get(id=rid)
    owndata.status=4
    owndata.save()
    return redirect("Admin:ViewOwnerList")    

                
def homepage(request):
    return render(request,"Admin/AdminHomePage.html")


def com(request):
    disdata=tbl_complainttype.objects.all()
    if request.method=="POST":
        tbl_complainttype.objects.create(complaint_name=request.POST.get("txt_complaint"))
        return render(request,"Admin/ComplaintType.html",{'complaint':disdata})
    else:
        return render(request,"Admin/ComplaintType.html",{'complaint':disdata})



def DeleteComplaint(request,did):
    tbl_complainttype.objects.get(id=did).delete()
    return redirect("Admin:ComplaintType")


