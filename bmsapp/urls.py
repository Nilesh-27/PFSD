from django.urls import path
from . import views

# . represents current directory

urlpatterns = [
    path("formdemo",views.formdemofunction,name="formdemo"),
    path("displayformdata",views.displayformdatafunction,name="displayformdata"),
    path("logindemo",views.logindemofunction,name="logindemo"),
    path("checklogindemo",views.checklogindemofunction,name="checklogindemo"),


    path("registration",views.registration,name="registration"),
    path("userlogin",views.userlogin,name="userlogin"),


    path("adddepartment",views.adddepartment,name="adddepartment"),

    path("updatedepartment",views.updatdepartment,name="updatedepartment"),

    path("deleteuser/<int:uid>",views.deleteuser,name="deleteuser"),

    path("setcookies",views.setcookies,name="setcookies"),

    path("getcookies",views.getcookies,name="getcookies"),





    path("", views.indexfunction, name="index"),
    path("registration",views.registration,name="registration"),
    path("userlogin",views.userlogin,name="userlogin"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),
    path("contactus",views.contactus,name="contactus"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("ipl",views.iplpage,name="ipl"),
    path("fifa",views.fifapage,name="fifa"),
    path("wwe",views.wwepage,name="wwe"),
    path("profile",views.profile,name="profile"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),
    path("userhome",views.userhome,name="userhome"),
    path("userlogout",views.userlogout,name="userlogout"),
    path("adminlogin",views.adminsite,name="adminlogin"),
    path("checkadminpage",views.checkadmin,name="checkadminpage"),
    path("viewusers",views.viewusers,name="viewusers"),


]
