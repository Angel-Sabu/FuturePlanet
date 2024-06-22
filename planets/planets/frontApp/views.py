from django.shortcuts import render


# Create your views here.
def indexpage(request):
    return render(request, "index.html")


def aboutpage(request):
    return render(request, "about.html")

def servicepage(request):
    return render(request, "service.html")

def academiccounselling(request):
    return render(request, "academic_counselling.html")

def collegeadd(request):
    return render(request, "College Admissionasst.html")
def careerplanning(request):
    return render(request, "careerplanning.html")

def scholarshipss(request):
    return render(request, "scholarships.html")

def medicalcourse(request):
    return render(request, "medical_courses.html")

def nursingcourse(request):
    return render(request, "nursingcourses.html")

def engineercourse(request):
    return render(request, "engineeringcourse.html")

def alliedcourse(request):
    return render(request, "alliedhealth.html")

def physiotherapycourse(request):
    return render(request, "physiotherapy.html")

def computerapp(request):
    return render(request, "computerapplication.html")

def commercecourse(request):
    return render(request, "commercecourse.html")

def othercourse(request):
    return render(request, "othercourses.html")

def contactpage(request):
    return render(request, "contact.html")

def medicalcollege(request):
    return render(request, "medical_colleges.html")


