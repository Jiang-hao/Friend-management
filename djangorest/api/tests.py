from django.test import TestCase
from api.models import Person, Friends
# Create your tests here.
class APITests(TestCase):

	def create_person(self, name):
		return Person.objects.create(name=name,post_message='',received_message='')

	def create_friends(self, person):
		return Friends.objects.create(person=person,friends='',blocked_friends='',follower='',follow='')

	def follow(self, requestor, target):
		target_person = Person.objects.get(name=target)
		friends_obj = Friends.objects.get(person=target_person)
		friends_obj.follower + ' ' + requestor
		friends_obj.save()

	def block(self, requestor, target):
		requestor_person = Person.objects.get(name=requestor)
		friends_obj = Friends.objects.get(person=target_person)
		friends_obj.block_friends + ' ' + requestor
		friends_obj.save()

	def test_connect_db(self):
		a = self.create_person('a')
		b = self.create_person('b')
		self.assertTrue(isinstance(a,Person))
		self.assertTrue(isinstance(b,Person))

		a_friends = self.create_friends(a)
		b_friends = self.create_friends(b)

		a_new_friends = a_friends.friends+' ' +b.name
		b_new_friends = b_friends.friends+' ' +a.name

		self.assertEqual(a_new_friends,' b')
		self.assertEqual(b_new_friends,' a')

	def test_follow_db(self):
		c = self.create_person('c')
		d = self.create_person('d')

		c_friends = self.create_friends(c)
		d_friends = self.create_friends(d)


		c_new_follow = c_friends.follow+' ' +d.name
		d_new_follower = d_friends.follower+' ' +c.name
		self.assertEqual(c_new_follow,' d')
		self.assertEqual(d_new_follower,' c')

	def test_block_db(self):
		e = self.create_person('e')
		f = self.create_person('f')

		e_friends = self.create_friends(e)
		f_friends = self.create_friends(f)


		e_new_block = e_friends.blocked_friends+' ' +f.name
		self.assertEqual(e_new_block,' f')