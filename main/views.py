from django.shortcuts import render, redirect
from main.forms import UserRegForm
from main.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from main.models import Leave

# Create your views here...
class LeaveCreateView(CreateView):
	model=Leave

	fields=["desc","type","leavedate"]
	success_url="/leaves/"
	def get(self,request):
		role=self.request.user.type
		if role.lower()=="m":
			self.fields=self.fields+["user"]
		return CreateView.get(self,request)
	#def post(self,request):
	#	import pdb;pdb.set_trace()
	#	CreateView.post(self,request)
	def form_valid(self,form):
		form_instance=form.instance 
		if "user" in form.data.keys():
			user_id=form.data.get('user')
			user_instance = User.objects.get(id=user_id)
			# user is a foreignkey in leave table. suppose to give instace of the user to
			# the leave table to insert the records.
			form_instance.user=user_instance
		else:
			form_instance.user=self.request.user
		form_instance.save()
		return redirect(self.success_url)
	

		

@login_required
def logout_view(request):
	logout(request)
	return redirect("/")
	
def home_view(request):
	msg=""
	if request.method=="POST":
		data=request.POST
		user = authenticate(username=data["username"], 
		password=data["password"])
		if user:
			#request.session.update({"username":user.username})
			login(request, user)
			url=request.GET.get("next","/index/")
			return redirect(url)
			msg="Login successfull"
		else:
			msg="Login failed"
	return render(request,"main/home.html",{"msg":msg})
def user_register(request):
	msg=""
	if request.method=="POST":
		form=UserRegForm(request.POST)
		if form.is_valid():
			form.save()
			user_instance=form.instance 
			user_instance.set_password(user_instance.password)
			user_instance.save()
			msg="User registered successfully"
		else:
			msg=form._errors
	form=UserRegForm()
	return render(request, "main/user_register.html",
		{"form":form,"msg":msg})
