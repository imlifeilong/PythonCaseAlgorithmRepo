import json

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def login(request):
    print(request.body)
    return HttpResponse(json.dumps({"msg": "everything ok."}))
