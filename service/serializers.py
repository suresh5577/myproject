from rest_framework import serializers
from main.models import Leave
import re
class LeavePOSTAPISerializer(serializers.ModelSerializer):
	class Meta:
		model=Leave 
		#fields = "__all_" or ["desc","user","leavetype","leavedate"]
		exclude=("date",)
	def validate_desc(self,value):
		if re.search("[^ ,.a-z0-9_-]",value,re.I):
			raise serializers.ValidationError("invalid description")
		return value
class LeaveGETAPISerializer(serializers.ModelSerializer):
	class Meta:
		model=Leave 
		fields = "__all__"
class LeavePUTAPISerializer(serializers.ModelSerializer):
	class Meta:
		model=Leave 
		#fields = "__all_" or ["desc","user","leavetype","leavedate"]
		exclude=("date",)
		extra_kwargs={"desc":{"required":False},
					  "type":{"required":False},
					   "leavedate":{"required":False},
					   "user":{"required":False},
		}

