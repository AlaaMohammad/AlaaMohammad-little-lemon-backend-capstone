from django.db import models
from django.shortcuts import render

# Create your models here.

def index(request):
    return render(request,'index.html',{})

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateField()

    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length= 255)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
