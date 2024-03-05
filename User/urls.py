from django.urls import path
from User import views

app_name='User'
urlpatterns = [ 
    path('userhome/',views.userhome,name="UserHome"),
    path('myprofile/',views.myprofile,name="MyProfile"), 
    path('editprofile/',views.editprofile,name="EditProfile"), 
    path('changepassword/',views.changepassword,name="ChangePassword"), 
    path('ajaxrent/',views.ajaxrent,name="ajaxrent"), 
    path('viewrents/',views.viewrents,name="ViewRents"), 
    path('usercomplaint/',views.complaint,name="UserComplaint"), 
    path('del_complaint/<int:did>',views.DeleteComplaint,name="del_complaint"),
    path('feedback/',views.feedback,name="Feedback"), 
    path('book/',views.book,name="book"), 
    path('userrequest/<int:rid>',views.userrequest,name="UserRequest"), 
    path('mybooking/',views.mybooking,name="MyBooking"),
    path('advancepayment/<int:rid>',views.advancepayment,name="AdvancePayment"),
    path('loader/',views.loader,name="Loader"),
    path('success/',views.success,name="Success"),
    path('userfeedback/',views.feedback,name="UserFeedback"), 
    path('del_feedback/<int:did>',views.DeleteFeedback,name="del_feedback"),
    path('shopstar/<int:mid>',views.starrating,name="shoprating"),
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('logout/',views.logout,name="logout"),

    path('Viewmore/<int:rid>',views.Viewmore,name="Viewmore"),


]    