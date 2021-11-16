from django.db import models
from django.db.models.deletion import CASCADE
import bcrypt 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class JavaManager(models.Manager):
    def shop_validator(self,postData):
        errors = {}
        if len(postData["name"]) < 3:
            errors["name"] = "  name must be at least 3 characters"
        if len(postData['street_address']) <6:
            errors['street_address'] = " address must be at least 6 characters"
        if len(postData['city']) <3:
            errors['city'] = " city must be at least 3 characters"
        if len(postData['state']) <2:
            errors['city'] = " state must be at least 2 characters"
        if len(postData['zip_code']) <5:
            errors['city'] = " Zip Code must be at least 5 characters"
        if len(postData['hours_of_operation']) <0:
            errors['city'] = " hours of operation must be included"
        if len(postData['phone_number']) <10:
            errors['city'] = " phone number must be at least 10 characters"
        return errors 
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
    JavaManager()

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['first_name']) < 2:
            errors['first_name'] = 'First Name must be at least 2 characters'
        if len(form['last_name']) < 2:
            errors['last_name'] = 'Last Name must be at least 2 chacters'
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Address'
        email_check = self.filter(email = form['email'])
        if email_check:
            errors['email'] = "Email already in Use"
        if len(form['password'])< 8:
            errors['password'] = 'Password must be at least 8 characters'
        # if form['password'] != form['confirm']:
        #     errors['password'] = 'Passwords do not match'
        return errors
    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False

        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def register(self, form):
        pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = form['first_name'],
            last_name = form['last_name'],
            email = form['email'],
            password = pw,
        )

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
    UserManager()

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





