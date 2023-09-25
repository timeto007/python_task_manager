from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from . import models


# Create your views here.

class non_comp_task_view(APIView):

    # view all non completed tasks
    def get(self,request,id=None):
        if id==None:
            item=models.non_comp_task_model.objects.all()
            serializer=serializers.taskSerializer(item, many=True)
            return Response(serializer.data)
        else:
            try:
                item=models.non_comp_task_model.objects.get(id=id)
            except Exception as e:
                return Response(f"Task with ID {id} not found",status=404)
            serializer=serializers.taskSerializer(item)
            return  Response(serializer.data,status=200)

    # posting the task and completing the task
    def post(self,request,id=None):
        if id==None:
            serializer = serializers.taskSerializer(data=request.data)
            if serializer.is_valid():
                if serializer.validated_data.get('task_name') == None:
                    return Response("where is ur task name!!!!", status=400)

                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors,status=400)
        else:
            try:
                item = models.non_comp_task_model.objects.get(id=id)
            except Exception as e:
                return Response(f"Task with ID {id} not found", status=404)

            non_comp_serializer=serializers.taskSerializer(item)
            comp_serializer=serializers.compSerializer(data=non_comp_serializer.data)
            if comp_serializer.is_valid():
                try:
                    print(comp_serializer.validated_data.get('task_completed_time'))
                    comp_serializer.save()
                    item.delete()
                    datetime_string = non_comp_serializer.data["task_created_time"]
                    task_created_time = datetime.strptime(datetime_string, '%I:%M:%S %p %d-%m-%Y')
                    datetime_string = comp_serializer.data["task_completed_time"]
                    task_completed_time = datetime.strptime(datetime_string, '%I:%M:%S %p %d-%m-%Y')
                    time_taken = task_completed_time - task_created_time

                    response_data = {
                        "message": "Task Completed",
                        "task_name": comp_serializer.data["task_name"],
                        "task_created_time":non_comp_serializer.data["task_created_time"],
                        "task_completed_time":comp_serializer.data["task_completed_time"],
                        "time_taken":str(time_taken)
                    }
                    return Response(response_data, status=201)
                except Exception as e:
                    return  Response(str(e),status=400)
            return Response(comp_serializer.errors,status=400)


    def patch(self,request,id):
        try:
            item=models.non_comp_task_model.objects.get(id=id)
        except Exception as e:
            return Response(f"Task with ID {id} not found", status=404)

        serializer=serializers.taskSerializer(item,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)

    def delete(self,request,id):
        try:
            item=models.non_comp_task_model.objects.get(id=id)
        except Exception as e:
            return Response(f"Task with ID {id} not found", status=404)
        serializer=serializers.taskSerializer(item)
        task=serializer.data["task_name"]
        item.delete()
        return  Response(f"Task {task} is DELETED ",status=200)