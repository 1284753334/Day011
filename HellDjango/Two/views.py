from django.http import HttpResponse
import random
from django.shortcuts import render

# Create your views here.
from .models import Student


def index(request):
   return HttpResponse('Two index')

def add_student(request):
   student=Student()
   student.s_nama = "jerry%d" % random.randrange(100)
   student.save()
   return HttpResponse("add_student Successful%s" %  student.s_nama)

def getstudent(request):
   students=Student.objects.all()
   # for i in students:
   #    print(i.s_nama)
   contexts={
      "hobby":"打游戏",
      "students":students,
   }
   #return HttpResponse("Student List")
   return render(request,"students List.html",context= contexts)

def updatestudent(request):
   student = Student.objects.get(pk=2)
   student.s_nama="Jack"
   student.save()
   return HttpResponse("student update successful")

def delstudent(request):
   student = Student.objects.get(pk=2)
   student.delete()
   return None