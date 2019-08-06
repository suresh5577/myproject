from django.shortcuts import render
class RequestTracker:
	def __init__(self, view):
		self.view=view
	def __call__(self, request):
		#print("befor sending to view..")
		resp = self.view(request)
		if resp.status_code==500:
			return render(request, "main/500.html")
		elif resp.status_code==404:
			return render(request, "main/404.html")
		#print("code to execute before response")
		return resp
