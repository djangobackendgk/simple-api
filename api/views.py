from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.


#model object - single student data
def student_detail(request,pk):
	stu1=Student.objects.get(id=pk)
	serial=StudentSerializer(stu1)
	json_data=JSONRenderer().render(serial.data)
	return HttpResponse(json_data,content_type='application/json')


#query set - all student data
def student_list(request):
	stu1=Student.objects.all()
	serial=StudentSerializer(stu1,many=True)
	json_data=JSONRenderer().render(serial.data)
	return HttpResponse(json_data,content_type='application/json')