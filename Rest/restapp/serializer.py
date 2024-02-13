
from rest_framework import serializers
from  .models import *
from django.contrib.auth.models import User



class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self,data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError('User name taken')
            
        if data['email']:
            if User.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError('User email taken')
        return data
            
    def create(self,validated_data):
        user = User.objects.create(username = validated_data['username'],email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
        print(validated_data)


class Loginserializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id','color_name']

class PersonSerializer(serializers.ModelSerializer):
    # color = ColorSerializer()
    class Meta:
        model = Person
        fields = '__all__'
        depth = 1


    def validate(self, data):

        special_characters = '!@#$%^&*()_+{}\[\]:;<>,.?/~`'
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError('name cannot contain special charecters')
        
        # if data['age'] < 18:
        #     raise serializers.ValidationError('age should be grater than 18')
        return data
    
