from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title':'Home Page',
        'bdata':'Welcome to jweb| Jodhapur',
        'clist':['PHP','Java','Django'],
        'numbers':[10,20,30,40,50],
        'student_details':[
            {'name':'Pradeep','phone':9774893479},
            {'name':'Sumedh','phone':9776834768}
        ]       
    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("Welcome to Jweb")

def course(request):
    return HttpResponse("Welcome to Jweb course")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def contactPage(request):
    return render(request,"contact.html")