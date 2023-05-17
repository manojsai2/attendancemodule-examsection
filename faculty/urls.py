from django.urls import path,include
from . import views


urlpatterns = [
    path('faculty/faclogin', views.faclogin, name='faclogin'),
    path('faculty/updatedindex', views.updatedindex, name='updatedindex'),
    path('faculty/updatedadd', views.updatedadd, name='updatedadd'),
    path('faculty/check-attendance-upload/', views.check_attendance_upload, name='check_attendance_upload'),
    path('faculty/submit-review/', views.submit_review, name='submit_review'),
    
]
