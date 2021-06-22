from django.test import TestCase
from .models import Client,Room,Reservation
# Create your tests here.



class ClientTestCase(TestCase):
	def setUp(self):
		Client.objects.create(rut_client="27778234-5", first_name="Pepito", last_name="Flores", phone="+56948791599", email="holahola@gmail.com")
	
	def test_client(self):
		pepito= Client.objects.get(rut_client="27778234-5")	

		self.assertEqual(pepito.rut_client,"27778234-5")
		self.assertEqual(pepito.first_name,"Pepito")
		self.assertEqual(pepito.last_name,"Flores")
		self.assertEqual(pepito.phone,"+56948791599")
		self.assertEqual(pepito.email,"holahola@gmail.com")


class RoomTestCase(TestCase):
	def setUp(self):
		Room.objects.create(numRoom="s")

	def test_numRoom(self):
		numRoom= Room.objects.get(numRoom="s")	

		self.assertEqual(numRoom.numRoom,"s")



		