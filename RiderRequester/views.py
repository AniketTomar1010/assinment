from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Rider,Requester,RegisterRider
from .serializers import RiderSerializer,RequesterSerializer,RequestFromRequesterSerializer

class RiderListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Rider items for given requested user
        '''
        rider = Rider.objects.all()
        serializer = RiderSerializer(rider, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Rider with given Rider data
        '''
        data = {
            'Name': request.data.get('Name'),
            'From_location': request.data.get('From_location'),
            'To_location': request.data.get('To_location'),
            'number_of_assets' : request.data.get('number_of_assets'),
            'Medium' : request.data.get ('Medium')
        }
        serializer = RiderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RequesterListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Requester items for given requested user
        '''
        requester = Requester.objects.all()
        serializer = RequesterSerializer(requester, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Requester with given Requester data
        '''
        data = {
            'Name': request.data.get('Name'),
            'From_location': request.data.get('From_location'),
            'To_location': request.data.get('To_location'),
            'number_of_assets' : request.data.get('number_of_assets'),
            'Type_of_assets' : request.data.get('Type_of_assets'),
            'Phone' : request.data.get('Phone'),
            'Sensitivities':request.data.get('Sensitivities')
        }
        serializer = RequesterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetRiderDetailsByLocationApiView(APIView):
    
    def get(self, request, *args, **kwargs):
        '''
        List all the Rider items for given requested
        '''
        rider = Rider.objects.filter(From_location = request.data.get('From_location'),
                                     To_location = request.data.get('To_location'),
                                     Timestamp__icontains=request.data.get('on_date')
                                     )
        if rider:
            serializer = RiderSerializer(rider, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("location not available", status=status.HTTP_400_BAD_REQUEST)


class RequestFromRequesterApiView(APIView):
    
    # 1. List all
    def get (self, request, *args, **kwargs) :
        '''
		List all the Rider items for given requested user
		'''
        register_rider = RegisterRider.objects.all()
        serializer = RequestFromRequesterSerializer(register_rider, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 2. Create
    def post (self, request, *args, **kwargs) :
        '''
		Create the Requester with given Requester data
		'''
        data = {
            'Rider' : request.data.get('Rider_id')
        }
        Requester_id=Requester.objects.filter(Phone=request.data.get('Requester_Phone')).first()
        
        if Requester_id.id:
             data["Requester"]=Requester_id.id
        else:
            return Response("requester or rider is not created", status=status.HTTP_400_BAD_REQUEST)
        serializer = RequestFromRequesterSerializer(data=data)
        if serializer.is_valid() :
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
