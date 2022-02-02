from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


############### USER PROFILE #####################
from profiles_api import models

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta: #to point to a specific model in our project 
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password') #list of filds that we want to manage via serializer; accessible in API-TUPLE       
        extra_kwargs = {
            'password': {
                'write_only': True, #password only 1st time, not amend or retrieve e.g. GET
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data): #OVERWRITE default create() function
        #so that password gets created with HASH not clear text as with default function 
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user


    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


#####################  PROFILE FEED #####################################################

class ProfileFeedItemSerializer(serializers.ModelSerializer): #Serializes profile feed items
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
        #set extra argument to a field e.g. read only 

#MODEL SERIALIZER - has save function assgned to it, used to save content of serializer to an object in the db  