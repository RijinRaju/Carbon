from pyexpat import model
from rest_framework import serializers
from .models import Emission

class InsertEmissionSerializer(serializers.ModelSerializer):
    

    class Meta:
        model= Emission
        fields = ['transportation','energyConsumption','foodConsumption','total']

    def create(self, validated_data):
        emission = Emission.objects.create(
            transportation = validated_data['transportation'],
            energyConsumption = validated_data['energyConsumption'],
            foodConsumption = validated_data['foodConsumption'],
            total = validated_data['transportation'] +validated_data['energyConsumption'] +validated_data['foodConsumption'],

        )
        
        return emission


class DisplayEmissionSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Emission
        fields = "__all__"
        depth = 1


class LimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emission
        fields = ["target","user"]