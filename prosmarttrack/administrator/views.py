
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
    

class Busstaff(View):   
    def get(self,request):
        return render(request,"administrator/busstaff/add_staff.html")   
    

class Students(View):
    def get(self,request):
        return render(request,"administrator/students/add_student.html")    
    
class AddStudents(View):
    def get(self,request):
        return render(request,"administrator/addstudents/add_addstudent.html")        

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

class Busdetails(View):
     def get(self,request):
        return render(request,"administrator/busdetails/add_bus.html")       


class Teachers(View):
    def get(self,request):
        return render(request,"administrator/teacher/add_teacher.html") 
    
class AddStudent(View):
     def get(self,request):
        return render(request,"administrator/student/add_student.html")  
     def post(self,request):
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully added"); window.location="/administrator/Viewstudent/"</script>''')  
        else:
            return HttpResponse('''<script>alert("invalid"); window.location="/administrator/Viewstudent"</script>''')  

class AddTeacher(View):
     def get(self,request):
        return render(request,"administrator/teacher/add_teacher.html")  
     def post(self,request):
        form=TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully added"); window.location="/administrator/Viewteacher/"</script>''')  
        else:
            return HttpResponse('''<script>alert("invalid"); window.location="/administrator/Viewteacher"</script>''')  


class AddBusco(View):
     def get(self,request):
        return render(request,"administrator/buscoordinators/add_buscoordinators.html")  
     def post(self,request):
        form=BuscooForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully added"); window.location="/administrator/Viewbusco/"</script>''')  
        else:
            return HttpResponse('''<script>alert("invalid"); window.location="/administrator/Viewbusco"</script>''')  

class AddGuardian(View):
     def get(self,request):
        return render(request,"administrator/guardian/add_guardian.html")  
     def post(self,request):
        form=GuardianForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully added"); window.location="/administrator/Viewguard/"</script>''')  
        else:
            return HttpResponse('''<script>alert("invalid"); window.location="/administrator/Viewguard"</script>''') 
        
class AddBusstaff(View):   
    def get(self,request):
        return render(request,"administrator/busstaff/add_staff.html")   
    def post(self,request):
        form=BusstaffForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully added"); window.location="/administrator/Viewbusstaff/"</script>''')  
        else:
            return HttpResponse('''<script>alert("invalid"); window.location="/administrator/Viewbusstaff"</script>''')
                

class AddBusdetails(View):   
    def get(self,request):
        return render(request,"administrator/busdetails/add_bus.html")   
    def post(self,request):
        form=BusdetailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully added"); window.location="/administrator/Viewbusdetails/"</script>''')  
        else:
            return HttpResponse('''<script>alert("invalid"); window.location="/administrator/Viewbusdetails"</script>''')
                

class AddaddStudent(View):
     def get(self,request):
        return render(request,"administrator/addstudents/add_addstudent.html")  
     def post(self,request):
        form=AddstudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully added"); window.location="/administrator/Viewaddstudent/"</script>''')  
        else:
            return HttpResponse('''<script>alert("invalid"); window.location="/administrator/Viewaddstudent"</script>''')  
        

class AddRoute(View):
     def get(self,request):
        return render(request,"administrator/route/add_route.html")     
     def post(self,request):
        form=RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully added"); window.location="/administrator/Viewroute/"</script>''')  
        else:
            return HttpResponse('''<script>alert("invalid"); window.location="/administrator/Viewroute"</script>''') 

class AddStation(View):
     def get(self,request):
        return render(request,"administrator/station/add_station.html")     
     def post(self,request):
        form=StationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully added"); window.location="/administrator/Viewstation/"</script>''')  
        else:
            return HttpResponse('''<script>alert("invalid"); window.location="/administrator/Viewstation"</script>''') 

class Addtransportation(View):
     def get(self,request):
        return render(request,"administrator/transpo/add_transpo.html")     
     def post(self,request):
        form=TranspoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully added"); window.location="/administrator/Viewtranspo/"</script>''')  
        else:
            return HttpResponse('''<script>alert("invalid"); window.location="/administrator/Viewtranspo"</script>''') 




        
        
      

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
        guard_obj =GuardianTable.objects.all()
        return render(request, "administrator/guardian/view_guardian.html", {'val': guard_obj})

class ViewBusstaff(View):
    def get(self, request):
        staff_obj =BusstaffTable.objects.all()
        return render(request, "administrator/busstaff/view_staff.html", {'val': staff_obj})        

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
    
class ViewaddStudent(View):
    def get(self, request):
        addstudent_obj =AddstudentTable.objects.all()
        return render(request, "administrator/addstudents/view_addstudent.html", {'val': addstudent_obj})        

class ViewBusdetails(View):
    def get(self, request):
        addbusdetails_obj =BusdetailsTable.objects.all()
        return render(request, "administrator/busdetails/view_bus.html", {'val': addbusdetails_obj})        


class EditTeacher(View):
    def get(self, request,id):
        a = TeacherTable.objects.get(id=id)
        print(a)
        return render(request, "administrator/teacher/edit_teacher.html", {'val': a}) 
    def post(self, request, id):
            obj = TeacherTable.objects.get(id=id)
            form = TeacherForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponse('''<script>alert("successfully edited"); window.location="/administrator/Viewteacher/"</script>''')    
                

class EditBusco(View):
    def get(self, request,id):
        a = BuscoordinatorsTable.objects.get(id=id)
        return render(request, "administrator/buscoordinators/edit_buscoordinators.html", {'val': a}) 
    def post(self, request, id):
            obj = BuscoordinatorsTable.objects.get(id=id)
            form = BuscooForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponse('''<script>alert("successfully edited"); window.location="/administrator/Viewbusco/"</script>''')  

class EditGuard(View):
    def get(self, request,id):
        a = GuardianTable.objects.get(id=id)
        return render(request, "administrator/guardian/edit_guardian.html", {'val': a}) 
    def post(self, request, id):
            obj = GuardianTable.objects.get(id=id)
            form = GuardianForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponse('''<script>alert("successfully edited"); window.location="/administrator/Viewguard/"</script>''') 
                         
class EditBusstaff(View):
    def get(self, request,id):
        a = BusstaffTable.objects.get(id=id)
        return render(request, "administrator/busstaff/edit_staff.html", {'val': a}) 
    def post(self, request, id):
            obj = BusstaffTable.objects.get(id=id)
            form = BusstaffForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                # return redirect('vstaff_page')
                return HttpResponse('''<script>alert("successfully edited"); window.location="/administrator/Viewbusstaff/"</script>''')

class EditStudent(View):
    def get(self, request,id):
        a = StudentTable.objects.get(id=id)
        print(a)
        return render(request, "administrator/student/edit_student.html", {'val': a}) 
    def post(self, request, id):
            obj = StudentTable.objects.get(id=id)
            form = StudentForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponse('''<script>alert("successfully edited"); window.location="/administrator/Viewstudent/"</script>''')    

class EditBusdetails(View):
    def get(self, request,id):
        a = BusdetailsTable.objects.get(id=id)
        print(a)
        return render(request, "administrator/teacher/edit_teacher.html", {'val': a}) 
    def post(self, request, id):
            obj = BusdetailsTable.objects.get(id=id)
            form = BusdetailForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponse('''<script>alert("successfully edited"); window.location="/administrator/Viewbusdetails/"</script>''')    
                               


class DeleteTeacher(View):
    def get(self,request,id):
        b=TeacherTable.objects.get(id=id)
        b.delete()
        return redirect('vteacher_page')
    
class DeleteBusco(View):
    def get(self,request,id):
        b=BuscoordinatorsTable.objects.get(id=id)
        b.delete()
        return redirect('vbusco_page')  
    
class DeleteGuardian(View):
    def get(self,request,id):
        b=GuardianTable.objects.get(id=id)
        b.delete()
        return redirect('vguard_page') 

class DeleteStudent(View):
    def get(self,request,id):
        b=StudentTable.objects.get(id=id)
        b.delete()
        return redirect('vstudent_page') 

class DeleteBusstaff(View):
    def get(self,request,id):
        b=BusstaffTable.objects.get(id=id)
        b.delete()
        return redirect('vstaff_page')        



class AdminDashboard(View):
     def get(self,request):
        return render(request,"administrator/admindashboard.html")       



    

        
    
    
    
      
      