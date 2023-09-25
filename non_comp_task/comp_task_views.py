from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from . import models

class comp_task_view(APIView):

    def get(self,request):

        item=models.comp_task_model.objects.all()
        serializer=serializers.compSerializer(item,many=True)
        return Response(serializer.data,status=200)