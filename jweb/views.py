from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from.forms import usersForm
from service.models import Service
from news.models import News
from django.core.paginator import Paginator

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
    servicesData=Service.objects.all()
    #for a in servicesData:
       # print(a.service_icon)
    #print(services)
    return render(request,"index.html")

def course(request):
    return HttpResponse("Welcome to Jweb course")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def contactPage(request):
    return render(request,"contact.html")

def headerPage(request):
    return render(request,"header.html")

def footerPage(request):
    return render(request,"footer.html")

def aboutMenu(request):
    return render(request,"Menu.html")

def aboutBase(request):
    return render(request,"Base.html")

def userForm(request):
    finalans=0
    fn=usersForm()
    data={'form':fn}
    try:
        if request.method=="POST":
        #n1=eval(request.POST['num1'])
        #n2=eval(request.POST['num2'])
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            finalans=n1+n2;
            data={
                'n1'==n1,
                'n2'==n2,
                'output'==finalans
            }
            url="/aboutThanks?output={}".format(finalans)
            return redirect(url)
    except:
        pass
    return render(request,"userForm.html",{'output':finalans})
def aboutThanks(request):
    return render(request,"Thanks.html")

def submitForm(request):
    finalans=0
    data={}
    try:
        if request.method=="POST":
        #n1=eval(request.POST['num1'])
        #n2=eval(request.POST['num2'])
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            finalans=n1+n2;
            data={
                'n1'==n1,
                'n2'==n2,
                'output'==finalans
            }
            
            return HttpResponse(request,finalans)
    except:
        pass; 
def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2;
            elif opr=="-":
                c=n1-n2;
            elif opr=="*":
                c=n1*n2;
            elif opr=="/":
                c=n1/n2;
    except :
        c="Invalid Operation"
    print(c)    
    return render(request,"calculator.html",{'c':c})  

#Even or Odd
def saveevenodd(request):
    c=''
    if request.method=="POST":
        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="Even Number";
        else:
            c="Odd Number";

    return render(request,"evenodd.html",{'c':c})

#markSheet   
def marksheet(request):
    if request.method=="POST":
        
        s1=eval(request.POST.get('subject1'))
        s2=eval(request.POST.get('subject2'))
        s3=eval(request.POST.get('subject3'))
        s4=eval(request.POST.get('subject4'))
        s5=eval(request.POST.get('subject5'))
        t=s1+s2+s3+s4+s5
        print(t)
        p=t*100/500;
        print(p)
        if p>=60:
            d="First Div"
        elif p>=48:
            d="Second Div"
        elif p>=38:
            d="Third Div"
        else:
            d="Fail"

        data={
            'total':t,
            'per':p,
            'div':d
        }
        
        return render(request,"marksheet.html",data)

    return render(request,"marksheet.html")
##Validator Code
def validatorFun(request):
    c=''
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render(request,"validate.html",{'error':True})
        
        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="Even Number";
        else:
            c="Odd Number";
    return render(request,"validate.html",{'c':c})
##Services Service calling 

def newsDetails(request,newsid):
    print(newsid)
    newsDetails=News.objects.get(id=newsid)
    data={
        'newsDetails':newsDetails
    }
    return render(request,"newsDetails.html",data)



def serviceAbout(request):
    #newsData=News.objects.all();
    ServiceData=Service.objects.all()
    paginator=Paginator(ServiceData,2)
    page_number=request.GET.get('page')
    ServiceDatafinal=paginator.get_page(page_number)
    totalpage=ServiceDatafinal.paginator.num_pages
    #if request.method=="GET":
        #st=request.GET.get('servicename')
        #if st!=None:
            #servicesData=Service.objects.filter(service_title__icontains=st)
    #for a in servicesData:
       #print(a.service_icon)
    #print(services)
    data={
        'servicesData':ServiceDatafinal,
        #'newsData' :newsData,
        'lastpage':totalpage,

    }
    return render(request,"index1.html",data)