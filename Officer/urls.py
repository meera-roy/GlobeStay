from django.urls import path
from Officer import views

app_name='Officer'
urlpatterns = [

     path('officerhome/',views.officerhome,name="OfficerHome"),
     path('myprofile/',views.myprofile,name="MyProfile"),
     path('Editprofile/',views.editprofile,name="Editprofile"),
     path('ChangePassword/',views.changepassword,name="ChangePassword"),  
     path('viewownerlist/',views.ownerlist,name="ViewOwnerList"),
     path('acceptedownerlist/',views.acceptedownerlist,name="AcceptedOwnerList"),
     path('rejectedownerlist/',views.rejectedownerlist,name="RejectedOwnerList"), 
     path('acceptowner/<int:aid>',views.acceptowner,name="acceptowner"),
     path('rejectowner/<int:rid>',views.rejectowner,name="rejectowner"),
     path('viewrent/',views.viewrent,name="ViewRent"),
     path('rejectedrent/',views.rejectedrent,name="rejectedrent"), 
     path('accptedrent/',views.acceptedrent,name="acceptedrent"), 
     path('rejectrent/<int:rid>',views.rejectrent,name="rejectrent"), 
     path('acceptrent/<int:aid>',views.acceptrent,name="acceptrent"), 
     path('viewcomplaint/',views.viewcomplaint,name="ViewComplaint"),     
     path('viewfeedback/',views.viewfeedback,name="ViewFeedback"),
     path('logout/',views.logout,name="logout"),   
     path('reply/<int:cid>', views.Reply, name="reply"),
     path('ureply/<int:cid>', views.uReply, name="ureply"),


]