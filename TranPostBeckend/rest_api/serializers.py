from rest_framework import serializers
from .models import employee,newemployee
class EmployeeSerializer(serializers.ModelSerializer):
    class  Meta:
        model=employee
        fields ='__all__'
class NEWEmployeeSerializer(serializers.ModelSerializer):
    class  Meta:
        model=newemployee
        fields ='__all__'




