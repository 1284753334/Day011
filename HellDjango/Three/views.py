

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
from .models import Student, Grade


def index(request):
    #return None
    three_index=loader.get_template('three_index.html')
    context={
        "student_name":"Sunck"
    }

    result = three_index.render(context=context)
    print(result)
    return HttpResponse(result)


def getgarden(request):
    stundent = Student.objects.get(pk=1)
    grade = stundent.s_grade
    return HttpResponse("Grade %s" %grade.g_name)