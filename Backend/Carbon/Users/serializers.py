from dataclasses import fields
from .models import User
from rest_framework import serializers


class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        


    def create(self,validated_data):

        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']

        )
        user.save()
        return user