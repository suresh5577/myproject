from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Leave, LeaveType, User
from django.core.cache import cache
from service.common import saveall
from service.serializers import LeavePOSTAPISerializer, LeaveGETAPISerializer,\
LeavePUTAPISerializer
from rest_framework import status

# Create your views here.
class LeaveAPI(APIView):
	authentication_classes=[]
	permission_classes=[]
	def post(self, request,format=None):
		data = self.request.data
		ser = LeavePOSTAPISerializer(data=data)
		if ser.is_valid():
			ser.save()
			msg="Leave created successfully"
			return Response(msg)
			
		else:

			msg=ser._errors
			return Response(msg,status=status.HTTP_400_BAD_REQUEST)
		
	def put(self, request, pk,format=None):
		leave_instance=Leave.objects.get(id=pk)
		data = self.request.data 
		ser = LeavePUTAPISerializer(data=data)
		if ser.is_valid():
			if "desc" in data:
				leave_instance.desc=data.get("desc")
			if "type" in data:
				type_inst=data.get("type")
				leave_instance.type=type_inst
			if "user" in data:
				user_instance=data.get("user")
				leave_instance.user=user_instance
			if "leavedate" in data:
				leave_instance.leavedate=data.get("leavedate")
			leave_instance.save()
			cache.delete("leave%s"%pk,)
			return Response("leave updated successfully!!")
		else:
			return Response(ser._errors,status=status.HTTP_400_BAD_REQUEST)


		
	def get(self, request,pk=None, format=None):
		#return Response("hello world")
		'''
		data = cache.get("leave%s"%pk,)
		if data:
			return Response(data)
		else:
			'''
		#import pdb;pdb.set_trace()
		if not pk:
			leaves=Leave.objects.all()
			
		if pk:
			leaves=Leave.objects.filter(id=pk)
		ser = LeaveGETAPISerializer(leaves,many=True)
		data = ser.data
		
		return Response(data)
	def delete(self,request, pk,format=None):
		leave_instance=Leave.objects.get(id=pk)
		leave_instance.delete()
		return Response("leave deleted successfully")

'''
class LeaveAPI(APIView):
	authentication_classes=[]
	permission_classes=[]
	def post(self, request,format=None):
		data = self.request.data
		type_id=data.get("type")
		leavetype_inst = LeaveType.objects.get(id=type_id)
		user_id=data.get("user")
		user_instance=User.objects.get(id=user_id)
		leave_instace=Leave(desc=data.get("desc"),
			type=leavetype_inst,
			leavedate=data.get("leavedate"),
			user=user_instance)
		leave_instace.save()
		#saveall(leave_instace)
		return Response("Leave created successfully")
	def put(self, request, pk,format=None):
		leave_instance=Leave.objects.get(id=pk)
		data = self.request.data 
		if "desc" in data:
			leave_instance.desc=data.get("desc")
		if "type" in data:
			type_id=data.get("type")
			leavetype_inst = LeaveType.objects.get(id=type_id)
			leave_instance.type=leavetype_inst
		if "user" in data:
			user_id=data.get("user")
			user_instance=User.objects.get(id=user_id)
			leave_instance.user=user_instance
		if "leavedate" in data:
			leave_instance.leavedate=data.get("leavedate")
		leave_instance.save()
		cache.delete("leave%s"%pk,)
		return Response("leave updated successfully!!")


		
	def get(self, request,pk=None, format=None):
		#return Response("hello world")
		data = cache.get("leave%s"%pk,)
		if data:
			return Response(data)
		else:
			if not pk:
				leaves=Leave.objects.all()
				
			if pk:
				leaves=Leave.objects.filter(id=pk)
			data = [{"id":obj.id,"description":obj.desc,"leavetype":obj.type.name,
			"leavedate":obj.leavedate,"applied":obj.user.username} for obj in leaves]
			cache.set("leave%s"%pk,data)
			return Response(data)
	def delete(self,request, pk,format=None):
		leave_instance=Leave.objects.get(id=pk)
		leave_instance.delete()
		return Response("leave deleted successfully")
'''