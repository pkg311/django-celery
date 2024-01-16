from django.shortcuts import render
from celeryProject.celery import  add
from myapp.Task import sub
from celery.result import AsyncResult

# Create your views here.
#Enqueue the task using delay
def home(request):
    result=add.delay(10,20)
    # result_value = result.get()
    print(result)


    return render(request,'home.html')

def contact(request):
    result=sub.apply_async(args=[80 ,10])
    print(result)
    return render(request,'contact.html',{'result':result})

def about(request):
    return render(request,'about.html')

def Check_result(request,task_id):
    result=AsyncResult(task_id)
    return render(request, 'result.html', {'result': result})
