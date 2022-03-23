from django.shortcuts import render
#rom . import serializers
from profiles_api import serializers
from rest_framework.response import Response
from rest_framework import status

#################################  VIEW SETS  ####################################
from rest_framework import viewsets

class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer   

    def list(self, request): # return a hello message
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


    def create(self, request): # new hello message
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)           

    def retrieve(self, request, pk): #getting an object by its ID
        return Response({'http_method': 'GET'})

    def update(self, request, pk):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk):
        return Response({'http_method': 'DELETE'})

###################################################   API VIEW   ####################################
from rest_framework.views import APIView

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None): #Returns a list of APIView features
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk=None):
       return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})

#################################  USER PROFILE -  PROFILE VIEW SETS - MODEL VIEW SET ##########################
from profiles_api import models

from rest_framework.authentication import TokenAuthentication # authentication and permission 
from profiles_api import permissions # authentication and permission 
from rest_framework import filters  # search profile feature 

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    
    authentication_classes = (TokenAuthentication, ) #authentication and permission 
    #you could add more authentications to this class
    permission_classes = (permissions.UpdateOwnProfile,) #authentication and permission 

    # so you may have an authenticated user who has permission to do certain things or use certain api's 
    # but not other api's (so use permission classes)    

    filter_backends = (filters.SearchFilter,) # search profile feature  (YOU CAN ADD MORE FILTERS)
    search_fields = ('name', 'email',) # search profile feature  (CLASS VARIABLE)

########################################## USER LOGIN API ###################################
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

##################################### PROFILE FEED API ############################################
#from rest_framework.permissions import IsAuthenticatedOrReadOnly #if not auth, then is read-only  ########### FIX ERROR slide 135 ##############
# DELETE READ ONLY
from rest_framework.permissions import IsAuthenticated
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,) # COMMA so it is going to be passed as a TUPLE
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    #permission_classes = (permissions.UpdateOwnStatus, IsAuthenticatedOrReadOnly) ########## FIX ERROR slide 135 ###########################
    # DELETE READ ONLY
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer): #overwrite/customise behaviour when creating an object 
        #function called every time when you do HTTP POST request to our ViewSet
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user) #set user profile

# perform_create() function called every time when you do HTTP POST request to our ViewSet
# MODEL SERIALIZER - has save function assigned to it, used to save content of serializer to an object in the db  
# USER_PROFILE gets saved in user profile, in addition to all items in serialiser that have been validated 
# because we've added the token authentication to ViewSet if the user has authenticated then the request will have 
# a user associated to the authenticated user so this user field gets added whenever the user is authenticated
# if they're not authenticated then it's just set to an anonymous user account


