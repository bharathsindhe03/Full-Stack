from django.contrib import admin
from myApp6.models import Course, Student 

@admin.register(Student) 
class StudentAdmin(admin.ModelAdmin): 
    list_display = ('student_name','student_usn','student_sem') 
    ordering=('student_name',) 
    search_fields = ('student_name',) 

@admin.register(Course) 
class CourseAdmin(admin.ModelAdmin): 
    list_display = ('course_code','course_name','course_credits') 
    ordering=('course_code',) 
    search_fields = ('course_code',) 

