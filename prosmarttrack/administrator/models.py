from django.db import models

# Create your models here.

class StudentTable(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    admissionno=models.CharField(max_length=10,null=True,blank=True)
    department=models.CharField(max_length=10,null=True,blank=True)
    sem=models.CharField(max_length=10,null=True,blank=True)
    email=models.CharField(max_length=10,null=True,blank=True)
    dob=models.CharField(max_length=10,null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    place=models.CharField(max_length=30,null=True,blank=True)
    presentstay=models.CharField(max_length=30,null=True,blank=True)
    guardianname=models.CharField(max_length=20,null=True,blank=True)
    phoneno=models.BigIntegerField(null=True,blank=True)
    transpotation=models.CharField(max_length=20,null=True,blank=True)
    busno=models.BigIntegerField(null=True,blank=True)
    busroute=models.CharField(max_length=20,null=True,blank=True)
    vehicleno=models.CharField(max_length=20,null=True,blank=True)
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
    guardianid=models.CharField(max_length=10,null=True,blank=True)
    studentid=models.CharField(max_length=10,null=True,blank=True)
    phoneno=models.BigIntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    


class RouteTable(models.Model):
    route=models.CharField(max_length=10,null=True,blank=True)
    status=models.CharField(max_length=10,null=True,blank=True)
    monthlycharges=models.BigIntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    


class StationTable(models.Model):
    route=models.ForeignKey(RouteTable, on_delete=models.CASCADE) 
    station=models.CharField(max_length=10,null=True,blank=True)
    status=models.CharField(max_length=10,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
class AddstudentTable(models.Model):
    STUDENT = models.ForeignKey(StudentTable, on_delete=models.CASCADE)
    STATION=models.ForeignKey(StationTable, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    



class TranspoTable(models.Model):
    STUDENT = models.ForeignKey(StudentTable, on_delete=models.CASCADE)
    ROUTE=models.ForeignKey(StationTable, on_delete=models.CASCADE)
    status=models.CharField(max_length=10,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    



    
   
   
     