from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .serializers import RoomSerializer
# from .models import RoomInfo
from rest_framework import status
from decimal import Decimal
import boto3
import json
import pyrebase
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


# @api_view(['GET', 'POST'])
# def upload(request, *args, **kwargs):
#     db = boto3.resource('dynamodb', aws_access_key_id="AKIARN3GXU7QILUU2IOW", aws_secret_access_key="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")
#     table = db.Table('picappDB')
    
#     if request.method == "GET":
#         roomInfos = table.scan() 
#         x = roomInfos.get('Items')
#         # print(x)
#         # return Response({'roomInfos': roomInfos.get('Items')})
#         print(len(x))
#         print(table.item_count)
#         return Response({'roomInfos': x})
#     elif request.method == "POST":
#         try:
#             newRoomInfos = request.data
#             newRoomInfos['length'] = round(Decimal(newRoomInfos['length']), 2)
#             newRoomInfos['width'] = round(Decimal(newRoomInfos['width']), 2)
#             newRoomInfos['height'] = round(Decimal(newRoomInfos['height']), 2)
#             print(len(newRoomInfos['images']))
#             table.put_item(Item=newRoomInfos)
#             # print(request.data)
#             # table.put_item(Item=request.data)
#             reponse = Response({'SUCCESS': "Data registered successfully !"}, status=status.HTTP_201_CREATED)
#             reponse['headers'] = {'Content-type':'application/json'}
#             return reponse
#         except:
#             print({'Error': "Failed to insert data"}    )
#             return Response({'Error':'Failed to insert'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


config = {
    "apiKey": "AIzaSyD_NsLv9xMJOGEhFg_Yg1MJz9iWm80cVJE",
    "authDomain": "roominfos-e7edb.firebaseapp.com",
    "databaseURL": "https://roominfors-e7edb.firebaseio.com",
    "projectId": "roominfos-e7edb",
    "storageBucket": "roominfos-e7edb.appspot.com",
    "messagingSenderId": "797506837870",
    "appId": "1:797506837870:web:e7bff7d003b7719fe2b57f"
}

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@api_view(['GET', 'POST'])
def upload(request, *args, **kwargs):
    if request.method == "GET":
        docs = db.collection("picappDB").get()
        myDocs = []
        
        for doc in docs:
            myDocs.append(doc.to_dict())
            
        return Response({'roomInfos': myDocs})
    elif request.method == "POST":
        try:
            newRoomInfos = request.data
            newRoomInfos['registrationDate'] = str(newRoomInfos['registrationDate'])
            newRoomInfos['length'] = round(float(newRoomInfos['length']), 2)
            newRoomInfos['width'] = round(float(newRoomInfos['width']), 2)
            newRoomInfos['height'] = round(float(newRoomInfos['height']), 2)
            print(type(newRoomInfos['registrationDate']))
            print(type(newRoomInfos['length']))
            print(type(newRoomInfos['width']))
            print(type(newRoomInfos['height']))
            print(type(newRoomInfos['images']))
            db.collection("picappDB").add(newRoomInfos)
            
            reponse = Response({'SUCCESS': "Data registered successfully !"}, status=status.HTTP_201_CREATED)
            reponse['headers'] = {'Content-type':'application/json'}
            return reponse
            # return Response({'success':'registered'})
        except:
            print({'Error': "Failed to insert data"}    )
            return Response({'Error':'Failed to insert'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
