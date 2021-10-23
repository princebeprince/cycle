from django.db import models
from colorfield.fields import ColorField


# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=250)
    logo  = models.ImageField(upload_to = 'media/logo')

    


class Cycles(models.Model):
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    model = models.CharField(max_length=250 , null=True , blank=True)
    model_color = ColorField(default='#FF0000', null=True , blank=True)
    frame = models.CharField(max_length=250, null=True , blank=True)
    frame_desc = models.CharField(max_length=250 , default='', null=True , blank=True)
    fork = models.CharField(max_length=250, null=True , blank=True)
    tyre_desc = models.CharField(max_length=250 , default='', null=True , blank=True)
    derailleur = models.CharField(max_length=250, null=True , blank=True)
    brake = models.CharField(max_length=250, null=True , blank=True)
    gear = models.CharField(max_length=250, null=True , blank=True)
    gear_desc = models.CharField(max_length=250 , default='', null=True , blank=True)
    wight_in_kg = models.CharField(max_length=250, null=True , blank=True)
    price_in_inr = models.IntegerField( null=True , blank=True)
    image = models.ImageField(upload_to = 'media/uploads')
    image_url = models.CharField(max_length=250 , default='', null=True , blank=True)


class StyleSettings(models.Model):
    css = models.TextField()
    html = models.TextField()


class Home(models.Model):
    text = models.CharField(max_length=250)
    image = models.ImageField('media/home')
