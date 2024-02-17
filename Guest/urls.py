from django.urls import path
from Guest import views

app_name='Guest'
urlpatterns = [ 
    path('ownerrgistration/',views.oreg,name="OwnerRegistration"),
    path('ajaxplace/',views.ajaxplace,name="ajaxplace"), 
    path('userrgistration/',views.ureg,name="UserRegistration"),
    path('ajaxplace/',views.ajaxplace,name="ajaxplace"), 
    path('login/',views.login,name="Login"),  
    path('',views.index,name="index"),  
]