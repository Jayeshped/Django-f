"""
URL configuration for jweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage),
    path('homePage/',views.homePage),
    path('aboutUs/',views.aboutUs),
    path('course/',views.course),
    path('course/<int:courseid>',views.courseDetails),
    path('contactPage/',views.contactPage),
    path('headerPage/',views.headerPage),
    path('footerPage/',views.footerPage),
    path('aboutMenu/',views.aboutMenu),
    path('aboutBase/',views.aboutBase),
    path('userForm/',views.userForm),
    path('submitForm/',views.submitForm,name="submitForm"),
    path('aboutThanks/',views.aboutThanks),
    path('calculator/',views.calculator),
    path('saveevenodd/',views.saveevenodd) ,
    path('marksheet/',views.marksheet),
    path('validatorFun/',views.validatorFun),
    path('servicesAbout/',views.servicesAbout),
    path('newsDetails/<newsid>',views.newsDetails),
   
]

