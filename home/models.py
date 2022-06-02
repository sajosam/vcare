# from email.mime import image
# from pyexpat import model
from django.db import models
import datetime
from cloudinary.models import CloudinaryField
# Create your models here.

class Hospital(models.Model):
    state_choices = (('kerala','kerala'),('demo','demo'))
    district_choices=(
        ('Kottayam','Kottayam'),
    )
    id   =models.AutoField(primary_key=True)
    h_name =models.CharField(max_length=100)
    slug =models.SlugField(max_length=200,unique=True)
    address =models.CharField(max_length=500)
    district =models.CharField(max_length=50,choices=district_choices)
    state =models.CharField(max_length=50,choices=state_choices)
    contact =models.BigIntegerField()
    description =models.CharField(max_length=500)
    email =models.EmailField(max_length=100, unique=True)
    is_active =models.BooleanField(default=True)
    date_of_joined=models.DateTimeField(default=datetime.datetime.now())
    h_image=CloudinaryField(max_length=100, blank=True)

    def __str__(self):
        return self.h_name

class Specialization(models.Model):
    id =models.AutoField(primary_key=True)
    s_name =models.CharField(max_length=50)
    slug =models.SlugField(max_length=200,unique=True)
    description =models.CharField(max_length=500)

    def __str__(self):
        return self.s_name


class Doctor(models.Model):
    id =models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=50)
    h_name =models.ForeignKey(Hospital,on_delete=models.CASCADE,null=True)
    s_name =models.ForeignKey(Specialization,on_delete=models.CASCADE,null=True)
    email= models.EmailField(max_length=100, unique=True)
    contact = models.BigIntegerField()
    d_image =CloudinaryField(max_length=50, blank=True)
    yos = models.IntegerField()
    dob =models.DateTimeField(default=datetime.datetime.now())
    fee =models.IntegerField() 
    sex=models.CharField(max_length=50)
    created_on =models.DateField(auto_now_add=True)
    qualification =models.CharField(max_length=500)
    is_active =models.BooleanField(default=True)

    def __str__(self):
        return self.d_name



class Appointment(models.Model):
    id =  models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=50)
    p_email = models.EmailField(max_length=100)
    p_contact = models.BigIntegerField()
    p_gender=models.CharField(max_length=100)
    p_age = models.IntegerField()
    d_name = models.CharField(max_length=100)
    h_name =models.CharField(max_length=100)
    s_name =models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=100)
    fee = models.IntegerField()
    symptoms = models.CharField(max_length=500)

    created_on = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.p_name

