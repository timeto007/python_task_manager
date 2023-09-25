from rest_framework import serializers
from . import models
class taskSerializer(serializers.ModelSerializer):
    task_created_time = serializers.DateTimeField(format="%I:%M:%S %p %d-%m-%Y", read_only=True)
    class Meta:
        model =models.non_comp_task_model
        fields = '__all__'

class compSerializer(serializers.ModelSerializer):
    task_completed_time = serializers.DateTimeField(format="%I:%M:%S %p %d-%m-%Y", read_only=True)
    class Meta:
        model=models.comp_task_model
        fields='__all__'
