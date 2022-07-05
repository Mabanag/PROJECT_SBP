from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Mainpage, name="Mainpage"),

    path('dashboard/',views.DashBoard, name="dashboard"),
    path('protektado_tayo_info/',views.Protektayo_Personal_Info, name="protektado_tayo_info"),
    path('delete_sbp/<int:sbpid>/',views.Delete_sbp_member, name = "delete_sbp"),
    path('edit_sbp/<int:sbpid>/',views.Edit_sbp_member, name = "edit_sbp"),
    path('update_sbp/<int:sbpid>/',views.Update_sbp_member, name = "update_sbp"),
   
    path('report_effects_surv/',views.Effects_Survey, name="report_effects_surv"),
    path('delete_effects/<int:sbpid>/',views.Delete_effects, name="delete_effects"),
    path('edit_effects/<int:sbpid>/',views.Edit_effects, name = "edit_effects"),
    path('update_effects/<int:sbpid>/',views.Update_effects, name = "update_effects"),

    path('report_positive_effects_surv/',views.Positive_Survey, name="report_positive_effects_surv"),
    path('delete_pos_effects/<int:sbpid>/',views.Delete_pos_effects, name = "delete_pos_effects"),
    path('edit_pos_effects/<int:sbpid>/',views.Edit_pos_effects, name = "edit_pos_effects"),
    path('update_pos_effects/<int:sbpid>/',views.Update_pos_effects, name = "update_pos_effects"),
   
    path('reports_notvac_surv/',views.Notvac_survey, name ="reports_notvac_surv"),
    path('delete_concerns/<int:sbpid>/',views.Delete_concerns, name="delete_concerns"),
    path('edit_concerns/<int:sbpid>/',views.Edit_concerns, name = "edit_concerns"),
    path('update_concerns/<int:sbpid>/',views.Update_concerns, name = "update_concerns"),


    path('feedback/',views.Feed_back, name ="feedback"),
    path('delete_message/<int:sbpid>/',views.Delete_message, name = "delete_message"),
    path('edit_message/<int:sbpid>/',views.Edit_message, name = "edit_message"),
    path('update_message/<int:sbpid>/',views.Update_message, name = "update_message"), 


    path('table_vaceff/',views.Table_Vaccination, name ="table_vaceff"),
    path('comments_message/',views. Comments_Message, name ="comments_message"),
    

    path('Vaccine_effect_updated/',views.Vaccine_effect_updated, name="Vaccine_effect_updated"),
    path('SBP_deleted/',views.SBP_deleted, name="SBP_deleted"),


    path('login_sbp/',views.Login_sbp, name="login_sbp"),
    path('logout_sbp/',views.Logout_sbp, name="logout_sbp"),


]
