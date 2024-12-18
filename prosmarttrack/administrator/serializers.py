from rest_framework.serializers import ModelSerializer
from .models import *



class Studentdetailserializer(ModelSerializer):
    class Meta:
        model = StudentTable
        fields = ['Name', 'admissionno', 'department', 'email','sem','dob','address','place','ph_no',
                  'guardianname','phoneno','transportation_type','commuter_type']
 

class Labdetailsserializer(ModelSerializer):
    class Meta:
        model = LabTable
        fields =['labname']

class Labattendanceserializer(ModelSerializer):
    class Meta:
        model = LabattendanceTable
        fields =['STUDENT','entrytime','exittime','period','status','LAB']

class Gatedetailsserializer(ModelSerializer):
    class Meta:
        model = GateTable
        fields =['STUDENT','date','entrytime','exittime']

class Teacherprofileserializer(ModelSerializer):
    class Meta:
        model = TeacherTable
        fields=['Name','teacherid','phoneno','department','designation','email']        

class Parentprofileserializer(ModelSerializer):
    class Meta:
        model = GuardianTable
        fields=['Name',  'admissionno', 'phoneno'] 

#transportation#

class Fineserializer(ModelSerializer):
    class Meta:
        model = FineTable
        fields=['reason',  'date', 'amount']  

class Paymenthistoryserializer(ModelSerializer):
    class Meta:
        model = PaymentTable
        fields=[ 'date', 'amount']   

class Busattendanceserializer(ModelSerializer):
    class Meta:
        model = BusattendanceTable
        fields =['STUDENT','date','entrytime','exittime','STATION']


            
        

        