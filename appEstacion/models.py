from django.db import models
from django import forms
import requests

# Create your models here.
class datoThingSpeak(models.Model):
    def _init_(self, request):
        self.request = request
        self.dato = self.enviar()

    def enviar(self):
        res = requests.get('https://api.thingspeak.com/channels/2013672/feeds.json?api_key=LVB3K48HOVEVHS0B&results=2')
        json = res.json()
        self.dato = json['feeds'][0]['field1'].split('r\n')
        self.dato=float(self.dato[0])
        
        return self.dato
