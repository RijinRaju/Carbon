from functools import partial
from signal import signal
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators  import api_view
from rest_framework import status
from .models import Emission
from .serializers import DisplayEmissionSeralizer, InsertEmissionSerializer,LimitSerializer
from django.utils import timezone
from django.dispatch import Signal, receiver

today = timezone.now().date()

carbon_limit_exceeded = Signal()

@api_view(['POST'])
def insert_emission(request):
    data = request.data
    data_dict = {
        'transportation':data.get('transportation',None),
        'energyConsumption':data.get('energyConsumption',None),
        'foodConsumption':data.get('foodConsumption',None),
        'total': int(data.get('transportation',None)) +int(data.get('energyConsumption',None))+int(data.get('foodConsumption',None))
    }
    try:
        print(today)
        emission = Emission.objects.get(date=today)
        print(emission)
        serializers = InsertEmissionSerializer(instance=emission,data=data_dict)
        if serializers.is_valid():
            serializers.save()
            if data_dict['total'] >= emission.target:
                carbon_limit_exceeded.send(sender=None, total_emissions=data_dict['total'])
                print(data_dict['total'])
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors)

    except:
        return Response(status=status.HTTP_304_NOT_MODIFIED)
           
@receiver(carbon_limit_exceeded)
def signal_indicator(sender,total_emissions,**kwargs):
    print(f"carbon limit exceeded:{total_emissions} tons of CO2 emitted.")
    return Response({"data":f"carbon limit exceeded:{total_emissions} tons of CO2 emitted."})


@api_view(['POST'])
def display_emission(request):
    total = []
    dates = []
    data = request.data
    user = data.get('user',None)
    
    emission_data = Emission.objects.filter(user = user)
    
    serializers = DisplayEmissionSeralizer(emission_data,many=True)
    
    for data in serializers.data:
        total.append(data['total'])
        dates.append(data['date'])
    print(total)
    return Response({'graph':total,'dates':dates})
   


@api_view(['POST'])
def set_limit(request):
    serializer = LimitSerializer(data = request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)  


@api_view(['POST'])
def compare_emission(request):
    data = Emission.objects.all()
    serializers = DisplayEmissionSeralizer(data,many=True)
    print(serializers.data)
    return Response(serializers.data)


@api_view(['POST'])
def admin_view(request):
    data = Emission.objects.all()
    serializers  = DisplayEmissionSeralizer(data,many=True)
    return Response(serializers.data)

@api_view(['POST'])
def delete_user(request):
    user = request.data.get('userid',None)
    print(user)
    delt = Emission.objects.get(user=user)
    delt.delete()
    return Response(status=status.HTTP_200_OK)
