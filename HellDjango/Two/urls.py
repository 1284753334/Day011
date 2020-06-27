from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^index/', views.index),
    url(r'^addstudent/',views.add_student),
    url(r'^getstudent/',views.getstudent),
    #url(r'^getstudent/',views.getstudent),
    url(r'^updatestudent/', views.updatestudent),
    url(r'^delstudent/', views.delstudent),


]