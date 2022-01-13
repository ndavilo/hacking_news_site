from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages


# Create your views here.

def member_views(request):
	all_members = Member.objects.all()
	context = {
		'all_m' : all_members,
	}
	return render(request, "members/members.html", context)

def join(request):
	if request.method == "POST":
		form = MemberForm(request.POST or None)
		if form.is_valid():
			form.save()
		else:
			firstname	=	request.POST['firstname']
			othernames	=	request.POST['othernames']
			age 		=	request.POST['age']
			email 		=	request.POST['email']
			passwd      =	request.POST['passwd']
			messages.success(request, ('Error try again'))
			return render(request, "members/join.html", {'firstname' :firstname,
				'othernames': othernames,
				'age':age,
				'email': email, 
				'passwd':passwd, 
				})
		messages.success(request, ('Submitted'))
		return redirect("home")

	else:
		return render(request, "members/join.html", {})
