from django.shortcuts import render
from django.http import HttpResponse
from sales.models import Customer

# Create your views here.
def cust(request):
	records = Customer.objects.all()
	return HttpResponse(records)

