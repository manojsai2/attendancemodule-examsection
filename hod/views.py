import csv
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect,reverse
from datetime import datetime, timedelta
from login.models import Department,Admin,Class,Student,Faculty,Calender,Course,Attendance,Teache,LateReport,Hod,AttendanceFrequency,Report
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404


# Create your views here.
fac=""
hod=""
dep=""
cla=""
cou=""
rea=""

def initial(hodt,dept):
    global hod,dep
    hod=hodt
    dep=dept
    return

def tial(clat,cout):
    global cla,cou
    cla=clat
    cou=cout
    return

def hodlogin(request):
    if request.method=="POST":
        u,p=request.POST.get('email'),request.POST.get('password')
        hodo=Hod.objects.filter(hod_id=u)
        if hodo.exists():
            if hodo.get().h_password==p:
                d=hodo.get().dept_id.dept_id
                initial(u,d)
                return hodindex(request)
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('index')
        else:
            messages.error(request, 'No such User exists')
            return redirect('index')
    else:
        messages.error(request, 'Enter Credentials')
        return redirect('index')
    
def hodindex(request):
    dept=Department.objects.filter(dept_id=dep)
    hodo=Hod.objects.filter(hod_id=fac)
    
    return render(request,'hodindex.html')

def set_frequency(request):
    if request.method == 'POST':
        frequency = request.POST['frequency']
        AttendanceFrequency.objects.create(frequency=frequency)
        messages.success(request, 'Attendance frequency set successfully!')
        return redirect('hodindex')
    return render(request, 'set_frequency.html')


def review_reports(request):
   

    reports = Report.objects.filter(is_approved=False)

    context = {
        'reports': reports,
    }

    return render(request, 'review_reports.html', context)

def approve_report(request):
   
    if request.method == 'POST':
        fac=request.POST['fac_id']
        print(fac)
        report =Report.objects.filter(report_id=fac)
        if report.exists():
          l= report.get().is_approved
          print(l)
          report.update(is_approved = True)
        #   report.save()
          messages.success(request, 'Report approved.')
        else:
         messages.error(request, 'Report not found!')
    return redirect('review_reports')



def reject_report(request):
        fac=request.POST['fac_id']
        print(fac)
        report =Report.objects.filter(report_id=fac)
        if report.exists():
          l= report.get().is_approved
          print(l)
          report.update(is_approved = True)
        #   report.save()
          messages.success(request, 'Report Rejected.')
        else:
         messages.error(request, 'Report not found!')
        return redirect('review_reports')
    