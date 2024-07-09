from django.shortcuts import render

# Create your views here.
def lists(request):
    student = ['abhiram','aravind','avinash']
    fruit = ['apple','banana','grape']
    context = {
        'student':student,
        'fruit':fruit
    }
    return render(request,'lists.html',context)
