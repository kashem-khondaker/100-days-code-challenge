from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse(" welcome to the task management system ")

def contact(request):
    return HttpResponse("this is contact page ...")

def show_task(request):
    return HttpResponse("this is out task page...")