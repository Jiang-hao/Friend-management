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
from django.template import loader
import datetime
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.shortcuts import render


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

def index(request):
	persons = Person.objects.all()
	context = {'allPersons': persons}
	if request.is_ajax():
		t = 'partial.html'
	else:
		t = 'index.html'
	#html = t.render(context)
	return render(request,t,context)


def listAll(request):
	res={}
	persons = Person.objects.all()
	context = {'allPersons': persons}
	return render(request,'templates/index.html',context)


@csrf_exempt
def connect(request):
	data = request.POST.getlist('friends[]')
	requestor = data[0]
	target = data[1]
	res={}
	try:
	 	if bool(Person.objects.filter(name=requestor)):
	 		#Record exists
	 		requestor_obj = Person.objects.get(name=requestor)
	 	else:
	 		#No records
	 		Person.objects.create(name=requestor,post_message='',receive_message='')
	 		requestor_obj = Person.objects.get(name=requestor)
	 		Friends.objects.create(person=requestor_obj,friends=[], blocked_friends=[],follower=[],follow=[] )


	 	if bool(Person.objects.filter(name=target)):
	 		#Record exists
	 		target_obj = Person.objects.get(name=target)
	 	else:
	 		#No records
	 		Person.objects.create(name=target,post_message='',receive_message='')
	 		target_obj = Person.objects.get(name=target)
	 		Friends.objects.create(person=target_obj,friends=[], blocked_friends=[],follower=[],follow=[] )
	 	
	 	try:
	 		#Record exists
	 		requestor_friends = Friends.objects.get(person=requestor_obj)
	 		if target not in requestor_friends.friends:
		 		requestor_friends.friends.append(target)
		 		requestor_friends.save()
		 		res['success'] = True
		 	else:
		 		res['success'] = False
		 		res['reason'] = target + " is already a friend of "+requestor
	 		
	 		target_friends = Friends.objects.get(person=target_obj)
	 		if requestor not in target_friends.friends:
		 		target_friends.friends.append(requestor)
		 		target_friends.save()
		 		res['success'] = True
		 	else:
		 		res['success'] = False
		 		res['reason'] = target + " is already a friend of "+requestor
	 	except Exception as e:
	 		res['success'] = False
	 		res['reason'] = "Error occured: "+ str(e) 
 	# try:
 	# 	requestor_friends = Friends.objects.get(person=requestor_obj)
 	# 	requestor_friends.friends.append(target)
 	# 	res['success'] = True
 	# except:
 	# 	res['success'] = False
 	# res['success'] = requestor_obj.name
	except Exception as e:
 		res['success'] = False
 		res['reason'] = "Error occured: "+ str(e)	
	return HttpResponse(json.dumps(res))

@csrf_exempt
def retrieve(request):
	res={}
	email = request.POST.get('email')
	try:
		the_person = Person.objects.get(name=email)

	except:
		res['success'] = False
		res['reason'] = email + " is not in Person database"
		return HttpResponse(json.dumps(res))
	try:
		friend_list = Friends.objects.get(person=the_person).friends
	except:
		res['success'] = False
		res['reason'] = email + " is not in Friends database"
		return HttpResponse(json.dumps(res))

	
	res['success'] = True
	res['friends'] = friend_list
	res['count'] = len(friend_list)

	return HttpResponse(json.dumps(res))


@csrf_exempt
def common(request):
	data = request.POST.getlist('friends[]')
	requestor = data[0]
	target = data[1]
	res={}
	try:
		requestor_person = Person.objects.get(name=requestor)

	except:
		res['success'] = False
		res['reason'] = requestor + " is not in Person database"
		return HttpResponse(json.dumps(res))
	try:
		target_person = Person.objects.get(name=target)

	except:
		res['success'] = False
		res['reason'] = target + " is not in Person database"
		return HttpResponse(json.dumps(res))

	try:
		requestor_friend_list = Friends.objects.get(person=requestor_person).friends
	except:
		res['success'] = False
		res['reason'] = requestor+" is not in Friends database"
		return HttpResponse(json.dumps(res))
	try:
		target_friend_list = Friends.objects.get(person=target_person).friends
	except:
		res['success'] = False
		res['reason'] = target+" is not in Friends database"
		return HttpResponse(json.dumps(res))
	
	commont_friends= list(set(requestor_friend_list).intersection(target_friend_list))	


	res['success'] = True
	res['friends'] = commont_friends
	res['count'] = len(commont_friends)

	return HttpResponse(json.dumps(res))

@csrf_exempt
def follow(request):
	
	res={}
	requestor = request.POST.get('requestor')
	target = request.POST.get('target')
	try:
		requestor_person = Person.objects.get(name=requestor)

	except:
		#Not in Person db. Create one for requestor
		Person.objects.create(name=requestor,post_message='',receive_message='')
		requestor_person = Person.objects.get(name=requestor)
		Friends.objects.create(person=requestor_person,friends=[],blocked_friends=[],follower=[],follow=[])
	

	try:
		target_person = Person.objects.get(name=target)

	except:
		#Not in Person db. Create one for requestor
		Person.objects.create(name=target,post_message='',receive_message='')
		target_person = Person.objects.get(name=target)
		Friends.objects.create(person=target_person,friends=[],blocked_friends=[],follower=[],follow=[])

	
	try:
		requestor_follow = Friends.objects.get(person=requestor_person)
		requestor_follow.follow.append(target)
		requestor_follow.save()

	except:
		res['success'] = False
		res['reason'] = requestor + " cannot follow "+ target
		return HttpResponse(json.dumps(res))
	

	try:
		target_follower = Friends.objects.get(person=target_person)
		target_follower.follower.append(requestor)
		target_follower.save()
	except:
		res['success'] = False
		res['reason'] = target + " cannot add " +requestor+" as follower"
		return HttpResponse(json.dumps(res))


	
	res['success'] = True

	return HttpResponse(json.dumps(res))



@csrf_exempt
def block(request):
	
	res={}
	requestor = request.POST.get('requestor')
	target = request.POST.get('target')
	try:
		requestor_person = Person.objects.get(name=requestor)

	except:
		#Not in Person db. Create one for requestor
		Person.objects.create(name=requestor,post_message='',receive_message='')
		requestor_person = Person.objects.get(name=requestor)
		Friends.objects.create(person=requestor_person,friends=[],blocked_friends=[],follower=[],follow=[])
	

	try:
		target_person = Person.objects.get(name=target)

	except:
		#Not in Person db. Create one for requestor
		Person.objects.create(name=target,post_message='',receive_message='')
		target_person = Person.objects.get(name=target)
		Friends.objects.create(person=target_person,friends=[],blocked_friends=[],follower=[],follow=[])

	
	try:
		requestor_blocks = Friends.objects.get(person=requestor_person)
		requestor_blocks.blocked_friends.append(target)
		requestor_blocks.save()

	except:
		res['success'] = False
		res['reason'] = requestor + " cannot block "+ target
		return HttpResponse(json.dumps(res))
	
	res['success'] = True

	return HttpResponse(json.dumps(res))