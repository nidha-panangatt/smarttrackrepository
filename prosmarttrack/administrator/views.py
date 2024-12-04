
from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import *
from .form import *

# Create your views here.
class LoginPage(View):
    def get(self, request):
        return render(request, "administrator/login.html")

class BusCoordinators(View):
    def get(self,request):
        return render(request,"administrator/buscoordinators/add_buscoordinators.html") 
    
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

class ViewBusco(View):
    def get(self, request):
        busco_obj =BuscoordinatorsTable.objects.all()
        return render(request, "administrator/buscoordinators/view_buscoordinators.html", {'val': busco_obj})        



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

class DeleteBusco(View):
    def get(self,request,id):
        b=BuscoordinatorsTable.objects.get(id=id)
        b.delete()
        return redirect('vbusco_page')  

class Guardian(View):
    def get(self,request):
        return render(request,"administrator/guardian/add_guardian.html") 

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


class ViewGuardian(View):
    def get(self, request):
        guard_obj =GuardianTable.objects.all()
        return render(request, "administrator/guardian/view_guardian.html", {'val': guard_obj})                
    
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

class DeleteGuardian(View):
    def get(self,request,id):
        b=GuardianTable.objects.get(id=id)
        b.delete()
        return redirect('vguard_page') 

class ViewStudentdetails(View):
    def get(self, request,id):

        obj =GuardianTable.objects.get(id=id)
        admission = obj.admissionno 
        student_obj = StudentTable.objects.get(admissionno=admission)
        print("%%%%%%%%%%%%", admission)
        return render(request, "administrator/guardian/student_det.html", {'val': student_obj})

class Busstaff(View):   
    def get(self,request):
        return render(request,"administrator/busstaff/add_staff.html")

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
        
class ViewBusstaff(View):
    def get(self, request):
        staff_obj =BusstaffTable.objects.all()
        print(staff_obj)
        return render(request, "administrator/busstaff/view_staff.html", {'val': staff_obj})                

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
    
class DeleteBusstaff(View):
    def get(self,request,id):
        b=BusstaffTable.objects.get(id=id)
        b.delete()
        return redirect('vstaff_page')        


    



class Station(View):
     def get(self,request):
        return render(request,"administrator/station/add_station.html")    

class Route(View):
     def get(self,request):
        return render(request,"administrator/route/add_route.html")  
     
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
        
class ViewRoute(View):
    def get(self, request):
        route_obj =RouteTable.objects.all()
        return render(request, "administrator/route/view_route.html", {'val': route_obj})        

class EditRoute(View):
    def get(self, request,id):
        a = RouteTable.objects.get(id=id)
        print(a)
        return render(request, "administrator/route/edit_route.html", {'val': a}) 
    def post(self, request, id):
            obj = RouteTable.objects.get(id=id)
            form = RouteForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponse('''<script>alert("successfully edited"); window.location="/administrator/Viewroute/"</script>''')    

class DeleteRoute(View):
    def get(self,request,id):
        b=RouteTable.objects.get(id=id)
        b.delete()
        return redirect('vroute_page')                                 


class Charges(View):
     def get(self,request):
        return render(request,"administrator/charges/add_charges.html")  
class ViewCharges(View):
    def get(self, request):
        charges_obj =ChargesTable.objects.all() # type: ignore
        return render(request, "administrator/charges/view_charges.html", {'val': charges_obj})        

 

class Transportation(View):
     def get(self,request):
        return render(request,"administrator/transpo/add_transpo.html")

class ViewTranspo(View):
    def get(self, request):
        transpo_obj =TranspoTable.objects.all()
        return render(request, "administrator/transpo/view_transpo.html", {'val': transpo_obj})        
    

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


     


class Busdetails(View):
     def get(self,request):
        return render(request,"administrator/busdetails/add_bus.html") 

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
                

class ViewBusdetails(View):
    def get(self, request):
        addbusdetails_obj =BusdetailsTable.objects.all()
        return render(request, "administrator/busdetails/view_bus.html", {'val': addbusdetails_obj})        

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


class DeleteBusdetails(View):
    def get(self,request,id):
        b=BusdetailsTable.objects.get(id=id)
        b.delete()
        return redirect('vbusdetail_page')  
    


    

    


class Teachers(View):
    def get(self,request):
        return render(request,"administrator/teacher/add_teacher.html") 
    
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

class ViewTeacher(View):
    def get(self, request):
        teacher_obj = TeacherTable.objects.all()
        return render(request, "administrator/teacher/view_teacher.html", {'val': teacher_obj})

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

class DeleteTeacher(View):
    def get(self,request,id):
        b=TeacherTable.objects.get(id=id)
        b.delete()
        return redirect('vteacher_page')                
    
class AddStudent(View):
     def get(self,request):
        r=RouteTable.objects.all()
        return render(request,"administrator/student/add_student.html",{'val':r})  
     def post(self,request):
            student_image=request.FILES['student_image']
            print(student_image)
            name=request.POST['Name']
            admission_no=request.POST['admissionno']
            department=request.POST['department']
            sem=request.POST['sem']
            email=request.POST['email']
            dob=request.POST['dob']
            address=request.POST['address']
            place=request.POST['place']
            ph_no=request.POST['ph_no']
            guardianname=request.POST['guardianname']
            phoneno=request.POST['phoneno']
            commuter_type=request.POST.get('commuter_type',None)
            print("commuter",commuter_type)
            transportation_type=request.POST.get('transportation_type',None)
            print("transportation",transportation_type)
            rou=request.POST.get('route',None)
            print("route",rou)
            
            obj = StudentTable()
            obj.student_image=student_image
            obj.Name = name
            obj.admissionno = admission_no
            obj.department = department
            obj.sem = sem
            obj.email = email
            obj.dob = dob
            obj.address = address
            obj.place = place
            obj.ph_no = ph_no
            obj.guardianname = guardianname
            obj.phoneno = phoneno
            obj.commuter_type = commuter_type
            obj.transportation_type = transportation_type
            obj.route = rou
            
            obj.save()
        
            return HttpResponse('''<script>alert("successfully added"); window.location="/administrator/Viewstudent/"</script>''')  
        # else:
        #     return HttpResponse('''<script>alert("invalid"); window.location="/administrator/Viewstudent"</script>''')  



class AddStudents(View):
    def get(self,request):
        return render(request,"administrator/addstudents/add_addstudent.html")   
    
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
        

class ViewaddStudent(View):
    def get(self, request):
        addstudent_obj =AddstudentTable.objects.all()
        return render(request, "administrator/addstudents/view_addstudent.html", {'val': addstudent_obj})        




class ViewStation(View):
    def get(self, request):
        Station_obj =StationTable.objects.all()
        return render(request, "administrator/station/view_station.html", {'val': Station_obj})      



class AddStation(View):
     def get(self,request):
        obj=RouteTable.objects.all()
        return render(request,"administrator/station/add_station.html",{'val':obj})     
     def post(self,request):
       
        form=StationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully added"); window.location="/administrator/routepoints"</script>''')  
        else:
            return HttpResponse('''<script>alert("invalid"); window.location="/administrator/Viewstation"</script>''') 

class EditStation(View):
    def get(self, request,id):
        a = StationTable.objects.get(id=id)
        b = RouteTable.objects.all()
        print(a)
        return render(request, "administrator/station/edit_station.html", {'val': a,'b':b}) 
    def post(self, request, id):
            obj = StationTable.objects.get(id=id)
            form = StationForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponse('''<script>alert("successfully edited"); window.location="/administrator/Viewstation/"</script>''')    


class DeleteStation(View):
    def get(self,request,id):
        b=StationTable.objects.get(id=id)
        b.delete()
        return redirect('vstation_page')                                                               





        
class Students(View):
    def get(self,request):
        return render(request,"administrator/students/add_student.html")

class ViewStudent(View):
    def get(self, request):
        student_obj =StudentTable.objects.all()
        return render(request, "administrator/student/view_student.html", {'val': student_obj})        
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


class DeleteStudent(View):
    def get(self,request,id):
        b=StudentTable.objects.get(id=id)
        b.delete()
        return redirect('vstudent_page') 
    
class routepoint1(View):
    def get(self,request):
        return render(request,'administrator/routepoint1.html')
    
     

    
    
    
        
class AdminDashboard(View):
     def get(self,request):
        return render(request,"administrator/admindashboard.html")       


class viewsTransportation(View):
    def get(self,request):
        r=RouteTable.objects.all()
        c=StationTable.objects.all()
        return render(request, 'administrator/transportation.html',{'r':r,'c':c})
    
class viewsRoutepoint(View):
     def get(self,request):
        r=RouteTable.objects.all()
        return render(request, 'administrator/routepoint.html',{'r':r})
     
class viewsDepartementstudents(View):
    def get(self,request,routeId,department):
        c=StudentTable.objects.filter(department=department).all()
        print(c)
        print(routeId)
        return render(request, "administrator/student/view_student copy.html", {'val': c,'routeId':routeId}) 
    
class AddDepartmentStudents(View):
    def post(self,request):
            print("hhhh")
            selected_students = request.POST.getlist('students')  # Get list of selected students
            route_id = request.POST.get('route_id')  # Get the selected route
            print(selected_students)
            print(route_id)


            route = StationTable.objects.get(id=route_id)  # Fetch route by ID

            # Loop through each selected student and create a record in TranspoTable
            for student_id in selected_students:
                student = StudentTable.objects.get(id=student_id)
                TranspoTable.objects.create(
                    STUDENT=student,
                    ROUTE=route,
                    status='Active',  # Default status, you can modify based on your logic
                )

            # Redirect to another page or render success message
            # Return JSON response with JavaScript to redirect outside the iframe
            return JsonResponse({'redirect_url': '/administrator/transportationss'})
 

    


class viewsStationbyroute(View):
    def get(self,request,route):
        d=StationTable.objects.filter(route=route).all()
        print(d)
        return render(request, "administrator/station/view_station copy.html", {'val': d})
  # Replace with your success page or URL name 
class viewsStationbyrouteid(View):
    def get(self,request,route):
        print("hhh")
        stations = StationTable.objects.filter(route=route).values('id', 'station')
        return JsonResponse({'stations': list(stations)})
    
    
# class viewsRoutedetails(View):
#     def get(self,request,route):
#         d=RouteTable.objects.filter(route=route).all()
#         return render(request, "administrator/route/view_route copy.html", {'val': d}) 
        
    





    
class viewsNotification(View):
     def get(self,request):
        return render(request, 'administrator/notification/notification.html')    
 





class viewsUnauthorizedaccess(View):
     def get(self,request):
        return render(request, 'administrator/notification/unau.html') 
     
class viewsPendingfee(View):
     def get(self,request):
        return render(request, 'administrator/notification/pending.html') 
     


        
    
    
    
      
      