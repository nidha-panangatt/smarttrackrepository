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
        fields = ['Name',  'admissionno', 'phoneno']

class BusstaffForm(ModelForm):
    class Meta:
        model = BusstaffTable
        fields = ['Name', 'staffid', 'route', 'phoneno']
        
class RouteForm(ModelForm):
    class Meta:
        model = RouteTable
        fields = ['route','tripno', 'status']
        
class StationForm(ModelForm):
    class Meta:
        model = StationTable
        fields = ['route', 'station', 'charges']

class StudentForm(ModelForm):
    class Meta:
        model = StudentTable
        fields = ['Name', 'admissionno', 'department', 'email','sem','dob','address','place','ph_no',
                  'guardianname','phoneno','transportation_type','commuter_type','route','vehicle_number',
                  'vehicle_type']
        
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



