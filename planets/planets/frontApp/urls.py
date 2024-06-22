from django.urls import path
from frontApp import views

urlpatterns = [

    path('indexpage/', views.indexpage, name="indexpage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('servicepage/', views.servicepage, name="servicepage"),
    path('academiccounselling/', views.academiccounselling, name="academiccounselling"),
    path('collegeadd/', views.collegeadd, name="collegeadd"),
    path('careerplanning/', views.careerplanning, name="careerplanning"),
    path('scholarshipss/', views.scholarshipss, name="scholarshipss"),
    path('medicalcourse/', views.medicalcourse, name="medicalcourse"),
    path('nursingcourse/', views.nursingcourse, name="nursingcourse"),
    path('engineercourse/', views.engineercourse, name="engineercourse"),
    path('alliedcourse/', views.alliedcourse, name="alliedcourse"),
    path('physiotherapycourse/', views.physiotherapycourse, name="physiotherapycourse"),
    path('computerapp/', views.computerapp, name="computerapp"),
    path('commercecourse/', views.commercecourse, name="commercecourse"),
    path('othercourse/', views.othercourse, name="othercourse"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('medicalcollege/', views.medicalcollege, name="medicalcollege"),

]