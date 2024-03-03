from django.urls import path
from Owner import views

app_name='Owner'
urlpatterns = [ 
    path('ownerhome/',views.ownerhome,name="OwnerHome"),
    path('myprofile/',views.myprofile,name="MyProfile"),
    path('editprofile/',views.editprofile,name="EditProfile"), 
    path('changepassword/',views.changepassword,name="ChangePassword"),
    path('rent/',views.rent,name="Rent"),
    path('del_rent/<int:did>',views.DeleteRent,name="del_rent"),
    path('rentgallery/<int:rid>',views.rentgallery,name="Rentgallery"),
    path('userbooking/',views.userbooking,name="UserBooking"),
    path('accepteduserbooking/',views.accepteduserbooking,name="accepteduserbooking"),
    path('rejecteduserbooking/',views.rejecteduserbooking,name="rejecteduserbooking"),
    path('acceptbook/<int:aid>',views.acceptbook,name="acceptbook"),
    path('rejectbook/<int:rid>',views.rejectbook,name="rejectbook"),
    path('ownercomplaint/',views.complaint,name="OwnerComplaint"), 
    path('del_complaint/<int:did>',views.DeleteComplaint,name="del_complaint"),
    path('logout/',views.logout,name="logout"),

]    