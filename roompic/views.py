from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RoomSerializer
from .models import RoomInfo
from rest_framework import status
from decimal import Decimal
import boto3
import json


@api_view(['GET', 'POST'])
def upload(request, *args, **kwargs):
    db = boto3.resource('dynamodb', aws_access_key_id="AKIARN3GXU7QMQE6ITO6", aws_secret_access_key="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")
    table = db.Table('roomInfos')
    
    if request.method == "GET":
        roomInfos = table.scan()
        x = roomInfos.get('Items')
        print(x)
        return Response({'roomInfos': roomInfos.get('Items')})
    elif request.method == "POST":
        try:
            newRoomInfos = request.data
            newRoomInfos['length'] = round(Decimal(newRoomInfos['length']), 2)
            newRoomInfos['width'] = round(Decimal(newRoomInfos['width']), 2)
            newRoomInfos['height'] = round(Decimal(newRoomInfos['height']), 2)
            print(newRoomInfos)
            table.put_item(Item=newRoomInfos)
            reponse = Response({'SUCCESS': "Data registered successfully !"}, status=status.HTTP_201_CREATED)
            reponse['headers'] = {'Content-type':'application/json'}
            return reponse
        except:
            print({'Error': "Failed to insert data"}    )
            return Response({'Error':'Failed to insert'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        