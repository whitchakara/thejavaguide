from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class JavaShop(models.Model):
    name= models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state= models.CharField(max_length=2)
    zip_code = models.IntegerField()
    hours_of_operation= models.IntegerField()
    phone_number = models.IntegerField()
    # 
    # reviews = models.ForeignKey(Review, related_name="reviews", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add="True")
    updated_at = models.DateTimeField(auto_now="True")

class User(models.Model):
    first_name= models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    user_name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    zip_code=models.IntegerField()
    password=models.CharField(max_length=50)
    # java_shops = models.ManyToManyField(JavaShop, related_name="shops")
    # review = models.ForeignKey(Review, related_name="reviews", on_delete = models.CASCADE)
    created_at=models.DateTimeField(auto_now_add="True")
    updated_at=models.DateTimeField(auto_now="True")

class Review(models.Model):
    ambience = models.IntegerField()
    cleanliness = models.IntegerField()
    coffee = models.IntegerField()
    music = models.IntegerField()
    location = models.IntegerField()
    additonal_comments = models.TextField()
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE ,blank= True, null=True)
    shop = models.ForeignKey(JavaShop, related_name="shops", on_delete=CASCADE, blank= True, null=True)
    created_at = models.DateTimeField(auto_now_add="True")
    updated_at = models.DateTimeField(auto_now="True")





