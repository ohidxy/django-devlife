from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from devlife.contact.models import Contact
from devlife.contact.serializers import ContactSerializer

def contact_data(request):
    if request.user.is_authenticated():   # When user is authenticated
        if request.method == 'GET':         # For viewing records
            contacts = Contact.objects.all().filter(user=1)
            contacts_serialized = ContactSerializer(contacts, many=True)
            return JsonResponse(contacts_serialized.data, safe=False,)
        elif request.method == 'POST':      # For creating a record
            pass
        elif request.method == 'DELETE':    # For deleting a record
            pass
    else: # When user is not authenticated 
        return HttpResponse("You are not authorized to access!")

# Create your views here.
