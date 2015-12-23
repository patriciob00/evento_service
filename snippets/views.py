from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.
class JSONResponse(HttpResponse):
    '''
    Um HttpResponse que renderiza seu conteudo em um JSON.
    '''

    def __init__(self, data, **kwargs):
        content =  JSONRenderer().render(data)
        kwargs['content_type'] = 'application/Json'
        super(JSONResponse, self).__init__(content, **kwargs)
