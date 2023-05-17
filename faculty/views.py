import csv
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect,reverse
from datetime import datetime, timedelta,date
from login.models import Department,Admin,Class,Student,Faculty,Calender,Course,Attendance,Teache,LateReport,Hod,AttendanceFrequency,Report,BTFacultyInfo,BTStudentInfo,BTCourses,BTFacultyAssignment,BTStudentRegistrations
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.http import Http404
from .forms import ReportForm

# Create your views here.
fac=""
dep=""
cla=""
cou=""
rea=""

def initial(fact,dept):
    global fac,dep
    fac=fact
    dep=dept
    return

def tial(clat,cout):
    global cla,cou
    cla=clat
    cou=cout
    return

def faclogin(request):
    if request.method=="POST":
        u,p=request.POST.get('email'),request.POST.get('password')
        faco=Faculty.objects.filter(fac_id=u)
        if faco.exists():
            if faco.get().f_password==p:
                d=faco.get().dept_id.dept_id
                initial(u,d)
                return updatedindex(request)
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('index')
        else:
            messages.error(request, 'No such User exists')
            return redirect('index')
    else:
        messages.error(request, 'Enter Credentials')
        return redirect('index')

# def updatedprofile(request):
#     if request.method=="POST":
#         try:
#             fact=Faculty.objects.filter(fac_id=fac)
#             fn=request.POST.get('fn')
#             ln=request.POST.get('ln')
#             pa=request.POST.get('pass')
#             if fn != "":
#                 Faculty.objects.filter(fac_id=fac).update(f_name=fn)
#             if ln !="" :
#                 Faculty.objects.filter(fac_id=fac).update(l_name=ln)
#             if pa !="" :
#                 Faculty.objects.filter(fac_id=fac).update(f_password=pa)
#             di=fact.get().dept_id.dept_id
#         except:
#             messages.error(request, 'Oops something went wrong!')
#             return redirect('updatedadd')
#     faco=Faculty.objects.filter(fac_id=fac)
#     dept=Department.objects.filter(dept_id=dep)
#     teach=Teache.objects.filter(fac_id=fac)
#     clas=[]
#     for i in teach:
#         clas.append([i.class_id.class_id,i.course_id.course_id])
#     return render(request,'updatedprofile.html',{'clas':clas,'fac':faco.get(),'dept':dept.get()})

# def editatt(request):
#     dept=Department.objects.filter(dept_id=dep)
#     faco=Faculty.objects.filter(fac_id=fac)
#     teach=Teache.objects.filter(fac_id=fac)
#     clao=Class.objects.filter(class_id=cla)
#     couo=Course.objects.filter(course_id=cou)
#     stud=Student.objects.all().filter(class_id=cla)
#     atte=Attendance.objects.all().filter(course_id=cou,fac_id=fac).order_by('-date')
#     if request.method=="POST":
#         dict=request.POST
#         for stud1 in stud:
#             if stud1.stud_id in dict.keys():
#                 if dict.get('bate'):
#                     try:
#                         a=Attendance.objects.filter(stud_id=stud1,fac_id=faco.get(),course_id=couo.get(),date=dict.get('bate')).get()
#                         if a.presence:
#                             p=0
#                         else:
#                             p=1
#                         Attendance.objects.filter(stud_id=stud1,fac_id=faco.get(),course_id=couo.get(),date=dict.get('bate')).update(presence=p)
#                         messages.success(request, 'Attendance Edited.')
#                     except:
#                         print(dict.get('bate').exists())
#                         messages.error(request, 'Value does not Exist')
#                         return redirect('updatedadd')
#     return redirect('updatedadd')


"""def take_report(request):
    late_reason = request.POST.get("late_reason")
    faco=Faculty.objects.filter(fac_id=fac)

    newinput=LateReport(late_reason = late_reason)
    newinput.save()
    return redirect(request,"")"""
     

def updatedindex(request):
    dept=Department.objects.filter(dept_id=dep)
    faco=Faculty.objects.filter(fac_id=fac)
    teach=Teache.objects.filter(fac_id=fac)
    clas=[]
    for i in teach:
        clas.append([i.class_id.class_id,i.course_id.course_id])
    return render(request,'updatedindex.html',{'clas':clas,'teach':teach})

def updatedadd(request): 
    
    dept=Department.objects.filter(dept_id=dep)
    faco=Faculty.objects.filter(fac_id=fac)
    teach=Teache.objects.filter(fac_id=fac)
    clas=[]
    for i in teach:
        clas.append([i.class_id.class_id,i.course_id.course_id])
    clao=Class.objects.filter(class_id=cla)
    couo=Course.objects.filter(course_id=cou)
    stud=Student.objects.all().filter(class_id=cla)
    atte=Attendance.objects.all().filter(course_id=cou,fac_id=fac).order_by('-date')
    if request.method=="POST":
        n=request.POST.get('classg')
        if n is not None:
            n,p=n[:n.find('$')],n[n.find('$')+1:]
            tial(n,p)
        dict=request.POST
        for stud1 in stud:
            if stud1.stud_id in dict.keys():
                p=0
            else:
                p=1
            if dict.get('bate'):
                try:
                    a=Attendance(stud_id=stud1,fac_id=faco.get(),course_id=couo.get(),date=dict.get('bate'),presence=p)
                    a.save()
                    messages.success(request, 'Attendance Added.')
                except:
                    messages.error(request, 'Value already Exists')
                    return redirect('updatedadd')
    clao=Class.objects.filter(class_id=cla)
    couo=Course.objects.filter(course_id=cou)
    stud=Student.objects.all().filter(class_id=cla)
    dept=Department.objects.filter(dept_id=dep)
    faco=Faculty.objects.filter(fac_id=fac)
    teach=Teache.objects.filter(fac_id=fac)
    if stud.exists():
        dept=stud.first().dept_id
    else:
        dept=dept.get()
    atte=Attendance.objects.all().filter(course_id=cou,fac_id=fac).order_by('-date')

    reason = request.POST.get("late_reason")
    faco=Faculty.objects.filter(fac_id=fac)

    newinput=LateReport(late_reason="reason")
    newinput.save()
    return render(request,'updatedadd.html',{'stud' : stud,'fac':faco.get(),'clat':clao.get(),'cout':couo.get(),'dept':dept,'atte':atte,'clas':clas})





def check_attendance_upload(request):
    last_upload = Attendance.objects.latest('date')
    upload_frequency = AttendanceFrequency.objects.get().frequency
    due_date = last_upload.date + timedelta(days=1)
    today = date.today()
    if today < due_date:
        return render(request, 'submit_report.html')
    else:
        return render(request, 'submit_report.html')


def submit_review(request):
    
  


    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            fac_id = form.cleaned_data['fac_id']
            faculty = Faculty.objects.get(fac_id=fac_id)            
            message = form.cleaned_data['message']
            report=Report(fac_id=faculty,message=message)
            report.save()
            messages.success(request, 'Report submitted successfully.')
            return redirect('updatedindex')
    else:
        form = ReportForm()

    context = {
        'form': form,
    }

    return render(request, 'submit_review.html', context)
