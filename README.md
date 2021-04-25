# Django-first app
Django first web application Using Python version 3.9 and Django Version 3.2
#prerequisites:
1.first we have to install Python Version.
2.After that install Django Version (Command pip install Django)
3.step1:first  we have to open the  command prompt and enter the first command (django-admin startproject project name)
4.step2: Createapp using this command (django-admin startapp app name)
5.step3:open urls.py file write the line path('',views.home,name='home') #project level
6.step4:open views.py file write the below code from django.http  import HttpResponse
     def home(request):
       	Response="<h1>Hi wellcome To  The Firstapp django web application</h1>"
	   return HttpResponse(Response)
7.Go to django project folder run server use this command py manage.py runserver
8.Output:
9.Hi wellcome To The Firstapp django web application

