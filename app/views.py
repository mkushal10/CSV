from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
import csv

# Create your views here.
def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="get_file.csv"'
    employees = Employee.objects.all()
    writer = csv.writer(response)
    for employee in employees:
        writer.writerow([employee.eno,employee.ename,employee.esalary,employee.eaddr])
    return response