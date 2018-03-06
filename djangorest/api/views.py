from django.shortcuts import render
import json
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from .serializers import *
from .models import *
from django.core import serializers
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

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
@csrf_exempt
def connect(request):

 	requestor = request.POST.get('requestor')
 	target = request.POST.get('target')
 	# res={}
 	# if bool(Person.objects.filter(name=requestor)):
 	# 	#Record exists
 	# 	requestor_obj = Person.objects.get(name=requestor)
 	# else:
 	# 	#No records
 	# 	Person.objects.create(name=requestor)
 	# 	requestor_obj = Person.objects.get(name=requestor)
 	# try:
 	# 	requestor_friends = Friends.objects.get(person=requestor_obj)
 	# 	requestor_friends.friends.append(target)
 	# 	res['success'] = True
 	# except:
 	# 	res['success'] = False
 	res={
 	'1':1,
 	'2':2
 	}
 	return HttpResponse(json.dumps(res))