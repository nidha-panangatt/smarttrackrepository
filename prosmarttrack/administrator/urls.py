

from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', LoginPage.as_view(), name="login_page"),
    path('admindash',AdminDashboard.as_view(),name="dashboard_page"),
    path('buscoordinator/',BusCoordinators.as_view(),name="buscoordinator_page"),
    path('teachers/',Teachers.as_view(),name="teacher_page"),
    path('guardian/',Guardian.as_view(),name="guardian_page"),
    path('busstaff/',Busstaff.as_view(),name="staff_page"),
    path('student/',Students.as_view(),name="student_page"),
    path('addstudent/',Students.as_view(),name="addstudent_page"),
    path('station/',Station.as_view(),name="station_page"),
    path('route',Route.as_view(),name="route_page"),
    #path('charges',Charges.as_view(),name="charges_page"),
    path('transportation',Transportation.as_view(),name="transportation_page"),
    path('busdetails',Busdetails.as_view(),name="busdetail_page"),

    path('addstudent',AddStudent.as_view(),name="addstudent_page"),
    path('addteacher',AddTeacher.as_view(),name="addteacher_page"),
    path('addbusco',AddBusco.as_view(),name="addbusco_page"),
    path('addguardian',AddGuardian.as_view(),name="addguardian_page"),
    path('addbusstaff',AddBusstaff.as_view(),name="addstaff_page"),
    path('addbusdetails',AddBusdetails.as_view(),name="addbusdetail_page"),
    path('addaddstudent',AddGuardian.as_view(),name="addaddstudent_page"),
    path('addroute',AddRoute.as_view(),name="addroute_page"),
    path('addstation',AddStation.as_view(),name="addstation_page"),
    path('addtransportation',Addtransportation.as_view(),name="addtransportation_page"),
    path('AddDepartmentStudents',AddDepartmentStudents.as_view(),name="AddDepartmentStudents"),


    path('Viewteacher/',ViewTeacher.as_view(),name="vteacher_page"),
    path('Viewbusco/',ViewBusco.as_view(),name="vbusco_page"),
    path('Viewguard/',ViewGuardian.as_view(),name="vguard_page"),
    path('Viewbusstaff/',ViewBusstaff.as_view(),name="vstaff_page"),
    #path('Viewcharges/',ViewCharges.as_view(),name="vcharges_page"),
    path('Viewroute/',ViewRoute.as_view(),name="vroute_page"),
    path('Viewstation/',ViewStation.as_view(),name="vstation_page"),
    path('Viewstudent/',ViewStudent.as_view(),name="vstudent_page"),
    path('Viewtranspo/',ViewTranspo.as_view(),name="vtranspo_page"),
    #path('Viewaddstudent/',ViewsAddstudent.as_view(),name="vaddstudent_page"),
    path('Viewbusdetails',ViewBusdetails.as_view(),name="vbusdetail_page"),
    path('Viewstudentdetails/<int:id>/',ViewStudentdetails.as_view(),name="vgsdetail_page"),

    
    path('editteacher/<int:id>/',EditTeacher.as_view(), name="eteacher_page"),
    path('editbusco/<int:id>/',EditBusco.as_view(),name="ebusco_page"),
    path('editguard/<int:id>/',EditGuard.as_view(),name="eguard_page"),
    path('editbusstaff/<int:id>/',EditBusstaff.as_view(),name="estaff_page"),
    path('editstudent/<int:id>/',EditStudent.as_view(),name="estudent_page"),
    path('editbusdetails/<int:id>/',EditBusdetails.as_view(),name="ebusdetails_page"),
    path('editbusroute/<int:id>/',EditRoute.as_view(),name="eroute_page"),
    path('editstation/<int:id>/',EditStation.as_view(),name="estation_page"),
    path('edittranspo/<int:id>/',EditTranspo.as_view(),name="etranspo_page"),
    
    
    
    
    path('Deleteteacher/<int:id>/',DeleteTeacher.as_view(),name='Dteacher_page'),
    path('Deletebusco/<int:id>/',DeleteBusco.as_view(),name='Dbusco_page'),
    path('Deleteguardian/<int:id>/',DeleteGuardian.as_view(),name='Dguardian_page'),
    path('Deletebusstaff/<int:id>/',DeleteBusstaff.as_view(),name='Dstaff_page'),
    path('Deletestudent/<int:id>/',DeleteStudent.as_view(),name='Dstudent_page'),
    path('Deletebusdetails/<int:id>/',DeleteBusdetails.as_view(),name='Ddetail_page'),
    path('Deletebusroute/<int:id>/',DeleteRoute.as_view(),name="Deletebusroute"),
    path('Deletestation/<int:id>/',DeleteStation.as_view(),name="Dstation_page"),
    # path('Deletetranspo/<int:id>/',DeleteTranspo.as_view(),name="Dtranspo_page"),

    

    path('transportationss', viewsTransportation.as_view(), name='transportationss'),
    path('routepoints', viewsRoutepoint.as_view(), name='routepoint'),
    path('departmentstudents/<int:routeId>/<str:department>/<int:stationId>',viewsDepartementstudents.as_view(),name='departmentstudentss'),
    path('save_student_station/',viewsDepartementstudents.as_view(),name='viewsDepartementstudents'),
    path('notifications', viewsNotification.as_view(), name='notifications'),
    path('stationbyroute/<str:route>/', viewsStationbyroute.as_view(), name='   '),
    path('stationbyrouteid/<str:route>/', viewsStationbyrouteid.as_view(), name='stationbyrouteid'),
    path('unauthorized/', viewsUnauthorizedaccess.as_view(), name='unauthorized_access'),
    path('pending/',viewsPendingfee.as_view(), name='pending_fee'),
    # path('routedetails/<str:route>/',viewsRoutedetails.as_view(), name='routedetails'),
   
]









    


