from django.shortcuts import render
import json
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from .serializers import *
from .models import *
from django.core import serializers
from django.http import JsonResponse

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

def listAll(request):
	res={}
	persons = Person.objects.all()
	for a in persons:
		friend_list = Friends.objects.filter(person = a)
		if(bool(friend_list)):
			# True if not empty
			res[a.name] = friend_list.get().friends
		else:
			res[a.name] = ['No friends']

	res['1'] = 1
	res['2'] = 3
	#data = serializers.serialize('json', res)
	return HttpResponse(json.dumps(res))
