from django.urls import path,include
from . import views


urlpatterns = [
    path('hod/hodlogin', views.hodlogin, name='hodlogin'),
    path('hod/hodindex', views.hodindex, name='hodindex'),
    path('hod/set_frequency', views.set_frequency, name='set_frequency'),
    path('hod/review-reports/', views.review_reports, name='review_reports'),
    path('hod/approve-report/', views.approve_report, name='approve_report'),
    path('hod/reject-report/', views.reject_report, name='reject_report'),
    
]
