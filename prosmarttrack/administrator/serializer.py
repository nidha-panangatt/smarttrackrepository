
from prosmarttrack.administrator.models import StudentTable



class Studentdetailserializer(ModelSerializer):
    class Meta:
        model = StudentTable
        fields = ['Name', 'admissionno', 'department', 'email','sem','dob','address','place','ph_no',
                  'guardianname','phoneno','transportation_type','commuter_type','route']
        