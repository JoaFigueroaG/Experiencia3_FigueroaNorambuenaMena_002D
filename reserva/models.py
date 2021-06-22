from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Client(models.Model):
    rut_client = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ['first_name']

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.first_name}'

class Room(models.Model):
    numRoom = models.CharField(max_length=3, primary_key=True)
    #client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)

    LOAN_STATUS = (
        ('s', 'Simple'),
        ('d', 'Doble'),
        ('p', 'Premium'),
    )

    typeRoom = models.CharField(
        max_length = 1,
        choices = LOAN_STATUS,
        blank = True,
        default = 's',
        help_text = 'Seleccion tipo de Paquete',
    )

    summary = models.TextField(max_length=1000, help_text='')

    def __str__(self):
        return self.numRoom

class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=6, help_text='Ingrese una ID unica')
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    checkIn = models.DateField(null=True, blank=True)
    checkOut = models.DateField(null=True, blank=True)

    
    


    
