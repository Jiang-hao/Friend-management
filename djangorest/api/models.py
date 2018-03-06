from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=50, unique=True, blank=False, primary_key=True)


class Friends(models.Model):
	person = models.ForeignKey(Person,on_delete=models.CASCADE)
	friends = ArrayField(
		models.CharField(max_length=50,null=True)
		)
	blocked_friends = ArrayField(
		models.CharField(max_length=50,null=True)
		)
	follows = ArrayField(
		models.CharField(max_length=50,null=True)
		) # Friends subscribe this person
	following = ArrayField(
		models.CharField(max_length=50,null=True)
		) # Friends this person subscribes