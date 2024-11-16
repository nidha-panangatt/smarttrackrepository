

from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LoginPage.as_view(), name="login_page"),
    path('buscoordinator/',BusCoordinators.as_view(),name="buscoordinator_page"),
    path('teachers/',Teachers.as_view(),name="teacher_page"),
    path('guardian/',Guardian.as_view(),name="guardian_page"),
    path('student/',Students.as_view(),name="student_page"),
    path('station/',Station.as_view(),name="station_page"),
    path('route',Route.as_view(),name="route_page"),
    path('charges',Charges.as_view(),name="charges_page"),
    path('transportation',Transportation.as_view(),name="transportation_page"),
    path('addstudent',AddStudent.as_view(),name="addstudent_page"),
    path('addteacher',AddTeacher.as_view(),name="addteacher"),
    path('addbusco',AddBusco.as_view(),name="addbusco_page"),
    path('addguardian',AddGuardian.as_view(),name="addguardian_page"),

    path('Vteacher/',ViewTeacher.as_view(),name="vteacher_page"),
    path('Vbusco/',ViewBusco.as_view(),name="vbusco_page"),
    path('Vguard/',ViewGuardian.as_view(),name="vguard_page"),
    path('Vcharges/',ViewCharges.as_view(),name="vcharges_page"),
    path('Vroute/',ViewRoute.as_view(),name="vroute_page"),
    path('Vstation/',ViewStation.as_view(),name="vstation_page"),
    path('Vstudent/',ViewStudent.as_view(),name="vstudent_page"),
    path('Vtranspo/',ViewTranspo.as_view(),name="vtranspo_page"),
    path('eteacher/<int:id>/',EditTeacher.as_view(),name="eteacher_page"),
    path('ebusco/<int:id>/',EditBusco.as_view(),name="ebusco_page"),
    path('admindash',AdminDashboard.as_view(),name="dashboard_page"),


]




    


