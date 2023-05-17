from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


DAYS_CHOICE=[('mon','Monday'),('tue','Tuesday'),('wed','Wednesday'),('thu','Thursday'),('fri','Friday'),('sat','Saturday'),]
LEAVE_CHOICE=[('ml','Medical Leave'),('od','On Duty')]

class Department(models.Model):
    dept_id = models.CharField(max_length=20,primary_key = True)
    dept_name = models.CharField(max_length=50)

class Admin(models.Model):
    admin_id = models.CharField(max_length=20,primary_key = True)
    password =models.CharField(max_length=30)

class Class(models.Model):
    class_id = models.CharField(max_length=20,primary_key=True)
    total_students = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(100)])
    

    
    

class Student(models.Model):
    stud_id = models.CharField(max_length=20,primary_key=True)
    s_password = models.CharField(max_length=30)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

class Faculty(models.Model):
    fac_id = models.CharField(max_length=20,primary_key=True)
    f_password = models.CharField(max_length=30)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)

class BTFacultyInfo(models.Model):
    FacultyId = models.IntegerField(default=100 , primary_key=True)
    f_password = models.CharField(max_length=30)
    Name = models.CharField(max_length=255)
    Phone = models.TextField()
    Email = models.CharField(max_length=255)
    Dept = models.IntegerField()
    Working = models.BooleanField()
    class Meta:
        db_table = 'BTFacultyInfo'
        constraints = [
            models.UniqueConstraint(fields=['FacultyId'], name='unique_BTfacultyinfo_facultyid')
        ]
        managed = True

class Hod(models.Model):
    hod_id = models.CharField(max_length=20,primary_key=True)
    h_password = models.CharField(max_length=30)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)

class Calender(models.Model):
    i=models.AutoField(primary_key=True)
    dates = models.DateField()
    day = models.CharField(max_length=9,choices=DAYS_CHOICE,default=None,blank=False)




class BTCourses(models.Model):
    SubCode = models.CharField(max_length=10)
    SubName = models.CharField(max_length=255)
    Credits = models.IntegerField()
    

    class Meta:
        db_table = 'BTCourses'
        constraints = [
            models.UniqueConstraint(fields = ['SubCode', 'SubName'], name='BTCourses_unique_course')
        ]
        managed = True


class Course(models.Model):
    course_id = models.CharField(max_length=20,primary_key=True)
    course_name = models.CharField(max_length=50)
    credits = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])


class Slot(models.Model):
    period_id=models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(8)],primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Holiday(models.Model):
    date = models.DateField(primary_key=True)
    description = models.CharField(max_length=100)



class Leave(models.Model):
    stud_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    leave_type = models.CharField(max_length=9,choices=LEAVE_CHOICE,default=None,blank=False)
    approved = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(1)])



class Timetable(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=9,choices=DAYS_CHOICE,default=None,blank=False)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    periods_id = models.ForeignKey(Slot, on_delete=models.CASCADE)
    class Meta:
        unique_together = (("class_id", "course_id","day","periods_id"),)


class BTFacultyAssignment(models.Model):
    Course = models.ForeignKey(BTCourses, on_delete=models.CASCADE)
    Faculty = models.ForeignKey('BTFacultyInfo', on_delete=models.CASCADE, related_name='faculty_facultyInfo')
    Section = models.CharField(max_length=2, default='NA')
    

    class Meta:
        db_table = 'BTFacultyAssignment'
        unique_together = (
            # ('Subject', 'RegEventId', 'Coordinator', 'Section'), 
            ('Course', 'Faculty', 'Section')
        )
        managed = True
   
class BTStudentInfo(models.Model):
    
    RegNo = models.IntegerField(primary_key=True)
    RollNo = models.IntegerField()
    Name = models.CharField(max_length=255)
    Dept = models.IntegerField()
    AdmissionYear = models.IntegerField()
    Section = models.ForeignKey(BTFacultyAssignment,on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'BTStudentInfo'
        constraints = [
            models.UniqueConstraint(fields=['RegNo'], name='unique_BTStudentInfo_RegNo'),
            models.UniqueConstraint(fields=['RollNo'], name='unique_BTStudentInfo_RollNo'),
        ]
        managed = True

class Teache(models.Model):
    fac_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    class Meta:
        unique_together = (("course_id", "class_id"),)

class LateReport(models.Model):
    late_reason = models.CharField(max_length=100, blank=True, null=True)
    
class AttendanceFrequency(models.Model):
    frequency = models.CharField(max_length=10)

class Report(models.Model):
    report_id = models.CharField(max_length=200, primary_key=True, default=datetime.now())
    fac_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    message = models.TextField()
    is_approved = models.BooleanField(default=False)

class BTStudentRegistrations(models.Model):
    RegId = models.IntegerField(primary_key=True)
    SubCode = models.ForeignKey(BTCourses , on_delete=models.CASCADE)
    Student = models.ForeignKey(BTStudentInfo , on_delete=models.CASCADE)
    Year = models.IntegerField()

class Attendance(models.Model):
    attendence_id = models.CharField(max_length=20,primary_key = True,default="")
    stu_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    fac_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    presence = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(1)])
    
    class Meta:
        unique_together = (("stu_id", "course_id","date"))

