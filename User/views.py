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
    rentdata=tbl_rent.objects.all()
    parray=[]
    for i in rentdata:
        rdata=tbl_rent.objects.get(id=i.id)
        sumdata=0
        totaldatacount=tbl_userrating.objects.filter(rent=rdata).count()
        totaldata=tbl_userrating.objects.filter(rent=rdata)
        for j in totaldata:
            sumdata=sumdata+int(j.rating_data)
        if totaldatacount>0:
            avg=sumdata//totaldatacount
        else:
            avg=0
        parray.append(avg)    
    renttype=tbl_renttype.objects.all()
    datas=zip(rentdata,parray)
    ar=[1,2,3,4,5]
    return render(request,"User/ViewRents.html",{'ar':ar,'rent':datas,'coudata':coudata,'stdata':stdata,'disdata':disdata,'pladata':pladata,'renttype':renttype})

def ajaxrent(request):
    ar=[1,2,3,4,5]
    if request.GET.get('rid')!="":
        renttypedata=tbl_renttype.objects.get(id=request.GET.get('rid'))
        if request.GET.get('pid')!="":
            placedata=tbl_place.objects.get(id=request.GET.get('pid'))
            rentdata=tbl_rent.objects.filter(owner__place=placedata,renttype=renttypedata)
            parray=[]
            for i in rentdata:
                rdata=tbl_rent.objects.get(id=i.id)
                sumdata=0
                totaldatacount=tbl_userrating.objects.filter(rent=rdata).count()
                totaldata=tbl_userrating.objects.filter(rent=rdata)
                for j in totaldata:
                    sumdata=sumdata+int(j.rating_data)
                if totaldatacount>0:
                    avg=sumdata//totaldatacount
                else:
                    avg=0
                parray.append(avg)    
            renttype=tbl_renttype.objects.all()
            datas=zip(rentdata,parray)
            return render(request,"User/ajaxrent.html",{'rent':datas,'ar':ar})
        elif request.GET.get('did')!="":
            districtdata=tbl_district.objects.get(id=request.GET.get('did'))
            rentdata=tbl_rent.objects.filter(owner__place__district=districtdata,renttype=renttypedata)
            parray=[]
            for i in rentdata:
                rdata=tbl_rent.objects.get(id=i.id)
                sumdata=0
                totaldatacount=tbl_userrating.objects.filter(rent=rdata).count()
                totaldata=tbl_userrating.objects.filter(rent=rdata)
                for j in totaldata:
                    sumdata=sumdata+int(j.rating_data)
                if totaldatacount>0:
                    avg=sumdata//totaldatacount
                else:
                    avg=0
                parray.append(avg)    
            renttype=tbl_renttype.objects.all()
            datas=zip(rentdata,parray)
            return render(request,"User/ajaxrent.html",{'rent':datas,'ar':ar})
        elif request.GET.get('sid')!="":
            statedata=tbl_state.objects.get(id=request.GET.get('sid'))
            rentdata=tbl_rent.objects.filter(owner__place__district__state=statedata,renttype=renttypedata)
            parray=[]
            for i in rentdata:
                rdata=tbl_rent.objects.get(id=i.id)
                sumdata=0
                totaldatacount=tbl_userrating.objects.filter(rent=rdata).count()
                totaldata=tbl_userrating.objects.filter(rent=rdata)
                for j in totaldata:
                    sumdata=sumdata+int(j.rating_data)
                if totaldatacount>0:
                    avg=sumdata//totaldatacount
                else:
                    avg=0
                parray.append(avg)    
            renttype=tbl_renttype.objects.all()
            datas=zip(rentdata,parray)
            return render(request,"User/ajaxrent.html",{'rent':datas,'ar':ar})    
        elif request.GET.get('cid')!="":
            countrydata=tbl_country.objects.get(id=request.GET.get('cid'))
            rentdata=tbl_rent.objects.filter(owner__place__district__state__country=countrydata,renttype=renttypedata)
            parray=[]
            for i in rentdata:
                rdata=tbl_rent.objects.get(id=i.id)
                sumdata=0
                totaldatacount=tbl_userrating.objects.filter(rent=rdata).count()
                totaldata=tbl_userrating.objects.filter(rent=rdata)
                for j in totaldata:
                    sumdata=sumdata+int(j.rating_data)
                if totaldatacount>0:
                    avg=sumdata//totaldatacount
                else:
                    avg=0
                parray.append(avg)    
            renttype=tbl_renttype.objects.all()
            datas=zip(rentdata,parray)
            return render(request,"User/ajaxrent.html",{'rent':datas,'ar':ar})
        else:
            rentdata=tbl_rent.objects.filter(renttype=renttypedata)
            parray=[]
            for i in rentdata:
                rdata=tbl_rent.objects.get(id=i.id)
                sumdata=0
                totaldatacount=tbl_userrating.objects.filter(rent=rdata).count()
                totaldata=tbl_userrating.objects.filter(rent=rdata)
                for j in totaldata:
                    sumdata=sumdata+int(j.rating_data)
                if totaldatacount>0:
                    avg=sumdata//totaldatacount
                else:
                    avg=0
                parray.append(avg)    
            renttype=tbl_renttype.objects.all()
            datas=zip(rentdata,parray)
            return render(request,"User/ajaxrent.html",{'rent':datas,'ar':ar})
    else:
        if request.GET.get('pid')!="":
            placedata=tbl_place.objects.get(id=request.GET.get('pid'))
            rentdata=tbl_rent.objects.filter(owner__place=placedata)
            parray=[]
            for i in rentdata:
                rdata=tbl_rent.objects.get(id=i.id)
                sumdata=0
                totaldatacount=tbl_userrating.objects.filter(rent=rdata).count()
                totaldata=tbl_userrating.objects.filter(rent=rdata)
                for j in totaldata:
                    sumdata=sumdata+int(j.rating_data)
                if totaldatacount>0:
                    avg=sumdata//totaldatacount
                else:
                    avg=0
                parray.append(avg)    
            renttype=tbl_renttype.objects.all()
            datas=zip(rentdata,parray)
            return render(request,"User/ajaxrent.html",{'rent':datas,'ar':ar})
        elif request.GET.get('did')!="":
            districtdata=tbl_district.objects.get(id=request.GET.get('did'))
            rentdata=tbl_rent.objects.filter(owner__place__district=districtdata)
            parray=[]
            for i in rentdata:
                rdata=tbl_rent.objects.get(id=i.id)
                sumdata=0
                totaldatacount=tbl_userrating.objects.filter(rent=rdata).count()
                totaldata=tbl_userrating.objects.filter(rent=rdata)
                for j in totaldata:
                    sumdata=sumdata+int(j.rating_data)
                if totaldatacount>0:
                    avg=sumdata//totaldatacount
                else:
                    avg=0
                parray.append(avg)    
            renttype=tbl_renttype.objects.all()
            datas=zip(rentdata,parray)
            return render(request,"User/ajaxrent.html",{'rent':datas,'ar':ar})
        elif request.GET.get('sid')!="":
            statedata=tbl_state.objects.get(id=request.GET.get('sid'))
            rentdata=tbl_rent.objects.filter(owner__place__district__state=statedata)
            parray=[]
            for i in rentdata:
                rdata=tbl_rent.objects.get(id=i.id)
                sumdata=0
                totaldatacount=tbl_userrating.objects.filter(rent=rdata).count()
                totaldata=tbl_userrating.objects.filter(rent=rdata)
                for j in totaldata:
                    sumdata=sumdata+int(j.rating_data)
                if totaldatacount>0:
                    avg=sumdata//totaldatacount
                else:
                    avg=0
                parray.append(avg)    
            renttype=tbl_renttype.objects.all()
            datas=zip(rentdata,parray)
            return render(request,"User/ajaxrent.html",{'rent':datas,'ar':ar})    
        else:
            countrydata=tbl_country.objects.get(id=request.GET.get('cid'))
            rentdata=tbl_rent.objects.filter(owner__place__district__state__country=countrydata)
            parray=[]
            for i in rentdata:
                rdata=tbl_rent.objects.get(id=i.id)
                sumdata=0
                totaldatacount=tbl_userrating.objects.filter(rent=rdata).count()
                totaldata=tbl_userrating.objects.filter(rent=rdata)
                for j in totaldata:
                    sumdata=sumdata+int(j.rating_data)
                if totaldatacount>0:
                    avg=sumdata//totaldatacount
                else:
                    avg=0
                parray.append(avg)    
            renttype=tbl_renttype.objects.all()
            datas=zip(rentdata,parray)
            return render(request,"User/ajaxrent.html",{'rent':datas,'ar':ar})


def complaint(request):
    uregdata=tbl_userregistration.objects.get(id=request.session['uid'])
    comdata=tbl_complainttype.objects.all()
    compdata=tbl_usercomplaint.objects.all()
    if request.method=="POST":
        com=tbl_complainttype.objects.get(id=request.POST.get("select_com"))
        tbl_usercomplaint.objects.create(
            
            complainttitle = request.POST.get("txt_name"),
            content = request.POST.get("txt_content"),
            complainttype=com,
            user=uregdata,

        )
        return render(request,"User/UserComplaint.html",{'uregdata':uregdata,'comdata':comdata,'compdata':compdata}) 
    else:
        return render(request,"User/UserComplaint.html",{'uregdata':uregdata,'comdata':comdata,'compdata':compdata})     

def DeleteComplaint(request,did):
    tbl_usercomplaint.objects.get(id=did).delete()
    return redirect("User:UserComplaint")


def feedback(request):
    feeddata=tbl_userfeedback.objects.all()
    userdata=tbl_userregistration.objects.get(id=request.session["uid"])
    if request.method=="POST":
        tbl_userfeedback.objects.create(    
            feedback = request.POST.get("txt_feedback"),
            user=userdata
        )
        return render(request,"User/UserFeedback.html",{'feeddata':feeddata}) 
    else:
        return render(request,"User/UserFeedback.html",{'feeddata':feeddata})





def starrating(request,mid):
    parray=[1,2,3,4,5]
    wdata=tbl_rent.objects.get(id=mid)
    counts=0
    counts=stardata=tbl_userrating.objects.filter(rent=wdata).count()
    if counts>0:
        res=0
        stardata=tbl_userrating.objects.filter(rent=wdata).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        return render(request,"User/ShopRating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/ShopRating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    workid=request.GET.get('workid')
    
    wdata=tbl_rent.objects.get(id=workid)
    tbl_userrating.objects.create(user_name=user_name,user_review=user_review,rating_data=rating_data,rent=wdata)
    stardata=tbl_userrating.objects.filter(rent=wdata).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})




def DeleteFeedback(request,did):
    tbl_userfeedback.objects.get(id=did).delete()
    return redirect("User:UserFeedback")

def book(request):
    uregdata=tbl_userregistration.objects.get(id=request.session['uid'])
    return render(request,"User/Book.html",{'uregdata':uregdata})      


def userrequest(request,rid):
    uregdata=tbl_userregistration.objects.get(id=request.session['uid'])
    rentdata=tbl_rent.objects.get(id=rid) 
    if request.method=="POST":
        datacount=tbl_userrequest.objects.filter(fromdate = request.POST.get("txt_fromdate"),
            todate = request.POST.get("txt_todate"),rent=rentdata).count()
        if datacount>0:
            return render(request,"User/UserRequest.html",{'uregdata':uregdata,'rentdata':rentdata,'msg':1})    
        else:
            tbl_userrequest.objects.create(
            file = request.FILES.get("txt_file"),
            content = request.POST.get("txt_content"),
            fromdate = request.POST.get("txt_fromdate"),
            todate = request.POST.get("txt_todate"),
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



def logout(request):
    del request.session["aid"]
    return redirect("Guest:Login")      


def Viewmore(request,rid):
    rentdata=tbl_rent.objects.get(id=rid)
    return render(request,"User/ViewMore.html",{'data':rentdata})