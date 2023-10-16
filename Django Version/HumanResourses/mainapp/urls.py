from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name = "index"),
    path("Main/",views.Main , name = "Main"),
    path("Login/",views.Login,name = "Login"),
    path("OTP/",views.OTP,name = "OTP"),
    path("ForgetPassword/",views.ForgetPassword ,name = "ForgetPassword"),
    
    path("AdminHome/",views.AdminHome ,name = "AdminHome"),
    path("AddEmploee/",views.AddEmploee ,name = "AddEmploee"),
    path("UpdateEmploee/",views.UpdateEmploee ,name = "UpdateEmploee"),
    path("RemoveEmploee/",views.RemoveEmploee ,name = "RemoveEmploee"),
    path("OrderVaction/",views.OrderVaction ,name = "OrderVaction"),
    
    path("ManagerHome/",views.ManagerHome ,name = "ManagerHome"),
    path("AddHR/",views.AddHR ,name = "AddHR"),
    path("UpdateHR/",views.UpdateHR ,name = "UpdateHR"),
    path("RemoveHR/",views.RemoveHR ,name = "RemoveHR"),
    path("AcceptionVactions/",views.AcceptionVactions ,name = "AcceptionVactions"),
    path("ShowHRs/",views.ShowHRs ,name = "ShowHRs"),

    path("ModifyPassword/",views.ModifyPassword ,name = "ModifyPassword"),
    path("ShowEmploees/",views.ShowEmploees ,name = "ShowEmploees"),
    path("ShowVactions/",views.ShowVactions ,name = "ShowVactions"),
]