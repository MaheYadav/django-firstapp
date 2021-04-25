from django.contrib import admin
from  .models import Student

class AdminStudent(admin.ModelAdmin):
    list_display = ['name','loc']

admin.site.register(Student,AdminStudent)
