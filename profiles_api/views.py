from rest_framework.views import APIview
from rest_framework.response import Response


# standard response object and import APIview class



class HelloApiView(APIview):
    """ Test API View"""

    def get(self, request, format = None):
        """ Returns a list of APIviews features"""
        an_apiview = [
        'Uses HTTP methods as functions (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logi',
        'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello World',
        'an_apiview': an_apiview})

        
