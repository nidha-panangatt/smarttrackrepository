
from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse

from .models import *
from .form import *

# Create your views here.
class LoginPage(View):
    def get(self, request):
        return render(request, "administrator/login.html")

class BusCoordinators(View):
    def get(self,request):
        return render(request,"administrator/buscoordinators/add_buscoordinators.html") 
    

    
class Guardian(View):
    def get(self,request):
        return render(request,"administrator/guardian/add_guardian.html")    
    

class Students(View):
    def get(self,request):
        return render(request,"administrator/students/add_student.html")    

class Station(View):
     def get(self,request):
        return render(request,"administrator/station/add_station.html")    

class Route(View):
     def get(self,request):
        return render(request,"administrator/route/add_route.html")  

class Charges(View):
     def get(self,request):
        return render(request,"administrator/charges/add_charges.html")   

class Transportation(View):
     def get(self,request):
        return render(request,"administrator/transpo/add_transpo.html")  


class Teachers(View):
    def get(self,request):
        return render(request,"administrator/teacher/add_teacher.html") 
    def post(self,request):
        form=TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"administrator/teacher/add_teacher.html")  
      
class AddStudent(View):
     def get(self,request):
        return render(request,"administrator/student/add_student.html")  
     def post(self,request):
        form=AddstudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"administrator/student/add_student.html")  

class AddTeacher(View):
     def get(self,request):
        return render(request,"administrator/teacher/add_teacher.html")  
     def post(self,request):
        form=AddstudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"administrator/teacher/add_teacher.html")  
        
class AddBusco(View):
     def get(self,request):
        return render(request,"administrator/buscoordinators/add_buscoordinators.html")  
     def post(self,request):
        form=AddstudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"administrator/buscoordinators/add_buscoordinators.html") 

class AddGuardian(View):
     def get(self,request):
        return render(request,"administrator/guardian/add_guardian.html")  
     def post(self,request):
        form=AddstudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"administrator/guardian/add_guardian.html")         


        
        
      

class ViewTeacher(View):
    def get(self, request):
        teacher_obj = TeacherTable.objects.all()
        return render(request, "administrator/teacher/view_teacher.html", {'val': teacher_obj})

    
class ViewBusco(View):
    def get(self, request):
        busco_obj =BuscoordinatorsTable.objects.all()
        return render(request, "administrator/buscoordinators/view_buscoordinators.html", {'val': busco_obj})        

class ViewGuardian(View):
    def get(self, request):
        guard_obj =BuscoordinatorsTable.objects.all()
        return render(request, "administrator/guardian/view_guardian.html", {'val': guard_obj})        

class ViewCharges(View):
    def get(self, request):
        charges_obj =ChargesTable.objects.all() # type: ignore
        return render(request, "administrator/charges/view_charges.html", {'val': charges_obj})        

class ViewRoute(View):
    def get(self, request):
        route_obj =RouteTable.objects.all()
        return render(request, "administrator/route/view_route.html", {'val': route_obj})        

class ViewStation(View):
    def get(self, request):
        Station_obj =StationTable.objects.all()
        return render(request, "administrator/station/view_station.html", {'val': Station_obj})      

class ViewStudent(View):
    def get(self, request):
        student_obj =StudentTable.objects.all()
        return render(request, "administrator/student/view_student.html", {'val': student_obj})        


class ViewTranspo(View):
    def get(self, request):
        transpo_obj =TranspoTable.objects.all()
        return render(request, "administrator/transpo/view_transpo.html", {'val': transpo_obj})        

class EditTeacher(View):
    def get(self, request,id):
        a = TeacherTable.objects.get(id=id)
        return render(request, "administrator/teacher/edit_teacher.html", {'val': a}) 
    def post(self, request, id):
            obj = TeacherTable.objects.get(id=id)
            form = TeacherForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                # return redirect('vteacher_page')
                return HttpResponse('''<script>alert("successfully edited"); window.location="/vteacher"</script>''')    
                

class EditBusco(View):
    def get(self, request,id):
        a = BuscoordinatorsTable.objects.get(id=id)
        return render(request, "administrator/buscoordinators/edit_buscoordinators.html", {'val': a}) 
    def post(self, request, id):
            obj = BuscoordinatorsTable.objects.get(id=id)
            form = BuscooForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                # return redirect('vbusco_page')
                return HttpResponse('''<script>alert("successfully edited"); window.location="/vteacher"</script>''')    

class AdminDashboard(View):
     def get(self,request):
        return render(request,"administrator/admindashboard.html") 
    
      
      