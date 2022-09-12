
from django.shortcuts import render
from django.http import HttpResponse
from src.database import Database
import json


def get_data(request):
    db = Database()
    head, data = db.get_from_database()    
    response = []
    response.append(head)
    response.append(data)
    json.dumps(response)
    

    return HttpResponse( json.dumps(response))
