from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    '''Test API View'''

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
