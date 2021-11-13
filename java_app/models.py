from django.db import models

# Create your models here.
class User(models.Model):
    first_name= models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    user_name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    zip_code=models.IntegerField()
    password=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add="True")
    updated_at=models.DateTimeField(auto_now="True")

class JavaShops(models.Model):
    name= models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state= models.CharField(max_length=2)
    zip_code = models.IntegerField()
    hours_of_operation= models.IntegerField()
    phone_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add="True")
    updated_at = models.DateTimeField(auto_now="True")
