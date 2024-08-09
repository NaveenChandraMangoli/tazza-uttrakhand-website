from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    category = models.CharField(max_length=50, default="")
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to= "images/", default= None, null=True)

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70,default="")
    phone = models.CharField(max_length=13,default="")
    address = models.CharField(max_length=150,default="")
    msg = models.CharField(max_length=300,default="")

    def __str__(self):
        return self.name
    
