from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers,models,permissions
from rest_framework import viewsets,filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


# Create your views here.
class HelloApiView(APIView):
    '''Test API View'''
    '''serializer class added so that, whenevrr sending post/patch request look out for name
        under serializer class
    '''
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        '''Returns a list of APIView features'''
        '''Uses HTTP methods as function(get,post,patch,delete) the apiview'''
        an_apiview=[
        'Uses HTTP methods as get post patch delete',
        'Is similar to traditional Django view',
        'Gives you most control over application logic',
        'Is mapped manually to URLs',

        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        '''Create a hello message with our name'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        '''Handle updating an object'''
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        '''Handle partial update of object'''
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        '''Delete an object'''
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    '''Test API viewset'''
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        '''Return a hello message'''

        a_viewset=[
            'Uses actions(list,create,retreive,update,partial_update)',
            'Automatically maps to URLs using routers',
            'more functionality,less code',

        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating profiles'''

    serializer_class=serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    '''used to search profile by name or id'''
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)

class UserLoginApiView(ObtainAuthToken):
    '''Handles creating user authentication tokens'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
