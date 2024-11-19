from django.forms import ModelForm

from .models import *



class BuscooForm(ModelForm):
    class Meta:
        model=BuscoordinatorsTable
        fields=['Name','coordinatorid','phoneno'] 

class TeacherForm(ModelForm):
    class Meta:
        model = TeacherTable
        fields = ['Name', 'teacherid', 'phoneno', 'department','designation','email']

class GuardianForm(ModelForm):
    class Meta:
        model = GuardianTable
        fields = ['Name', 'studentname', 'studentid', 'phoneno']

class BusstaffForm(ModelForm):
    class Meta:
        model = BusstaffTable
        fields = ['Name', 'id', 'route', 'phoneno']




        
class RouteForm(ModelForm):
    class Meta:
        model = RouteTable
        fields = ['route', 'status','monthlycharges']
        
class StationForm(ModelForm):
    class Meta:
        model = StationTable
        fields = ['route', 'station', 'status']

class StudentForm(ModelForm):
    class Meta:
        model = StudentTable
        fields = ['Name', 'admissionno', 'department', 'email','sem','dob','address','place','ph_no','presentstay','guardianname','phoneno','transpotation','busno','busroute','vehicleno']
        
class TranspoForm(ModelForm):
    class Meta:
        model = TranspoTable
        fields = ['STUDENT', 'ROUTE','status']

class AddstudentForm(ModelForm):
    class Meta:
        model = AddstudentTable
        fields = ['STUDENT', 'STATION']

class BusdetailForm(ModelForm):
    class Meta:
        model = BusdetailsTable
        fields = ['route', 'vehicleno','staff']        



