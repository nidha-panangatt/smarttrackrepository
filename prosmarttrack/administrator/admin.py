from msilib import Table
from django.contrib import admin

from administrator.models import *

# Register your models here.
admin.site.register(BuscoordinatorsTable),
admin.site.register(TeacherTable),
admin.site.register(GuardianTable),
admin.site.register(BusstaffTable),
admin.site.register(AddstudentTable),

admin.site.register(RouteTable),
admin.site.register(StationTable),
admin.site.register(StudentTable),
admin.site.register(TranspoTable),
admin.site.register(BusdetailsTable)





