import csv
from django.template import loader
from django.contrib import admin
from .models import Department,Admin,Class,BTStudentInfo,Student,BTFacultyInfo,Faculty,BTCourses,Course,Attendance,Teache,BTFacultyAssignment,LateReport,AttendanceFrequency,Hod,Report,BTStudentRegistrations
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.contrib import messages
from django.urls import path
from django.db import models
from django.contrib.auth.models import Permission

admin.site.register(Permission)


admin.site.site_header = 'Admin'
admin.site.site_title = 'Smart Attendance Manager |'
admin.site.index_title = ""

class AttendanceD(models.Model):
    class Meta:
        verbose_name_plural = 'Attendance Report'
        app_label = 'login'

def my_custom_view(request):
    a=[1]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="AttendanceReport.csv"'
    atte=Attendance.objects.all().order_by('stud_id','course_id','date')
    writer = csv.writer(response)
    writer.writerow(['Stud-Id','Faculty-Id','Dept','Course-Id','Date(dd-mm-yyyy)','Status'])
    for i in atte:
        if i.presence:
            writer.writerow([i.stud_id.stud_id,i.fac_id.fac_id,i.stud_id.dept_id.dept_id,i.course_id.course_id,i.date,'Present'])
        else:
            writer.writerow([i.stud_id.stud_id,i.fac_id.fac_id,i.stud_id.dept_id.dept_id,i.course_id.course_id,i.date,'Absent'])
    return response

class DummyModelAdmin(admin.ModelAdmin):
    model = AttendanceD
    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('my_admin_path/', my_custom_view, name=view_name),
        ]

class StudAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        return fields

class FacAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        return fields
class DataAdmin(admin.ModelAdmin):
    pass



admin.site.register(Student,StudAdmin)
admin.site.register(BTStudentInfo)
admin.site.register(AttendanceD, DummyModelAdmin)
admin.site.register(Department)
admin.site.register(Class)
admin.site.register(Faculty,FacAdmin)
admin.site.register(BTFacultyInfo)
admin.site.register(Course)
admin.site.register(BTCourses)
admin.site.register(Attendance)
admin.site.register(AttendanceFrequency)
admin.site.register(LateReport)
admin.site.register(Hod)
admin.site.register(Report)
admin.site.register(Teache)
admin.site.register(BTFacultyAssignment)
admin.site.register(BTStudentRegistrations)
admin.site.unregister(User)
admin.site.unregister(Group)

