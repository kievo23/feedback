from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CommentForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from companies.models import Company
from django.contrib import messages

# Create your views here.
@login_required(login_url= "/admin/login/")
def comment_create(request):
	form = CommentForm(request.POST or None)	

	#GET THE COMPANY DATA
	company = Company.objects.get(pk=request.GET.get('company_id'))
	context = {
		"form" : form,
		"company_id" : request.GET.get('company_id'),
		"company" : company
	}

	if request.method == "POST":
		form.company_id = request.GET.get('company_id')
		if form.is_valid():
			instance = form.save()
			form = CommentForm()
			messages.success(request, "Feedback Stored Successfully")
			context = {
				"form" : form,
				"message" : "records successfully",
				"company" : company
			}

	return render(request, "feedback.html",context)

