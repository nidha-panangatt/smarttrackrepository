from django.db import models

# Create your models here.

class StudentTable(models.Model):
    student_image=models.FileField(upload_to='student_image',null=True,blank=True)
    Name = models.CharField(max_length=30, null=True, blank=True)
    admissionno=models.CharField(max_length=10,null=True,blank=True)
    department=models.CharField(max_length=10,null=True,blank=True)
    sem=models.CharField(max_length=10,null=True,blank=True)
    email=models.CharField(max_length=10,null=True,blank=True)
    dob=models.CharField(max_length=10,null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    place=models.CharField(max_length=30,null=True,blank=True)
    ph_no=models.BigIntegerField(null=True,blank=True)
    guardianname=models.CharField(max_length=20,null=True,blank=True)
    phoneno=models.BigIntegerField(null=True,blank=True)
    commuter_type=models.CharField(max_length=20,null=True,blank=True)
    transportation_type=models.CharField(max_length=20,null=True,blank=True)
    route=models.CharField(max_length=20,null=True,blank=True)
   
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    


class BuscoordinatorsTable(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    coordinatorid=models.CharField(max_length=10,null=True,blank=True)
    phoneno=models.BigIntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    


class TeacherTable(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    teacherid=models.CharField(max_length=10,null=True,blank=True)
    phoneno=models.BigIntegerField(null=True,blank=True)
    department=models.CharField(max_length=30, null=True, blank=True)
    designation=models.CharField(max_length=30, null=True, blank=True)
    email=models.CharField(max_length=30, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    

class GuardianTable(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    admissionno=models.CharField(max_length=10,null=True,blank=True)
    phoneno=models.BigIntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class BusstaffTable(models.Model):  
     Name = models.CharField(max_length=30, null=True, blank=True)
     staffid=models.CharField(max_length=10,null=True,blank=True)
     route=models.CharField(max_length=20,null=True,blank=True)
     phoneno=models.BigIntegerField(null=True,blank=True)
     created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
     updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class RouteTable(models.Model):
    route=models.CharField(max_length=10,null=True,blank=True)
    tripno=models.BigIntegerField(null=True,blank=True)
    status=models.CharField(max_length=10,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
class BusdetailsTable(models.Model): 
    route=models.ForeignKey(RouteTable, on_delete=models.CASCADE,null=True,blank=True) 
    station=models.CharField(max_length=100,null=True,blank=True)
    vehicleno=models.CharField(max_length=50,null=True,blank=True)
    capacity=models.BigIntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    


class StationTable(models.Model):
    route=models.ForeignKey(RouteTable, on_delete=models.CASCADE) 
    station=models.CharField(max_length=10,null=True,blank=True)
    charges=models.BigIntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
class AddstudentTable(models.Model):
    STUDENT = models.ForeignKey(StudentTable, on_delete=models.CASCADE)
    STATION=models.ForeignKey(StationTable, on_delete=models.CASCADE)
    status=models.CharField(max_length=10,null=True,blank=True,default='active')
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
class TranspoTable(models.Model):
    STUDENT = models.ForeignKey(StudentTable, on_delete=models.CASCADE)
    status=models.CharField(max_length=10,null=True,blank=True)

class PaymentTable(models.Model):
    STUDENT = models.ForeignKey(AddstudentTable, on_delete=models.CASCADE)
    date=models.CharField(max_length=10,null=True,blank=True)
    STATION=models.ForeignKey(StationTable, on_delete=models.CASCADE)







    
   
   
     