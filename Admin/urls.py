from django.urls import path
from Admin import views

app_name='Admin'
urlpatterns = [ 
     path('country/',views.cou,name="Country"),
     path('homepage/',views.homepage,name="homepage"),
     path('del_country/<int:did>',views.DeleteCountry,name="del_country"),
     path('edit_country/<int:eid>',views.EditCountry,name="edit_country"),
     path('renttype/',views.ren,name="RentType"),
     path('del_renttype/<int:did>',views.DeleteRentType,name="del_renttype"),
     path('state/',views.sta,name="State"),
     path('del_state/<int:did>',views.DeleteState,name="del_state"),
     path('ajaxstate/',views.ajaxstate,name="ajaxstate"),
     path('district/',views.dis,name="district"),
     path('del_district/<int:did>',views.DeleteDistrict,name="del_district"),
     path('ajaxdistrict/',views.ajaxdistrict,name="ajaxdistrict"),
     path('place/',views.pla,name="place"),
     path('del_place/<int:did>',views.DeletePlace,name="del_place"),
     path('officer/',views.reg,name="Officer"),
     path('viewownerlist/',views.ownerlist,name="ViewOwnerList"),
     path('acceptedownerlist/',views.acceptedownerlist,name="AcceptedOwnerList"),
     path('rejectedownerlist/',views.rejectedownerlist,name="RejectedOwnerList"),
     path('acceptowner/<int:aid>',views.acceptowner,name="acceptowner"),
     path('rejectowner/<int:rid>',views.rejectowner,name="rejectowner"),
     path('Complaint/',views.com,name="ComplaintType"),
     path('del_complaint/<int:did>',views.DeleteComplaint,name="del_complaint"),


]