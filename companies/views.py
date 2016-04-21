from django.shortcuts import render
from companies.models import Company
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url= "/admin/login/")
def companies(request):
	data = Company.objects.filter(employee_id=request.user)
	context = {
		'data' : data
	}
	return render(request, "companies.html" ,context)

def home(request):
	return render(request, "home.html" ,{})