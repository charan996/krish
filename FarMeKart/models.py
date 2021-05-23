from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
#from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
from datetime import date
from django.contrib.auth.models import AbstractUser,User



class User(AbstractUser):
	t = (
		(1,'Farmer'),
		(2,'Customer'),
		(3,'guest'),
		)
	role = models.IntegerField(default=3,choices=t)
	g=[('M',"Male"),('F','Female')]
	h=[('P',"Passbook"),('A',"adhar")]
	age=models.IntegerField(default=10)
	gender=models.CharField(max_length=10,choices=g)
	proof_type=models.CharField(max_length=10,choices=h,default=0)
	impf=models.ImageField(upload_to='profiles/',default="profile.jpg")
	mobile_number=models.CharField(null=True,default="1234567890",max_length=10)
	address=models.CharField(max_length=200,default="Tirupathi")
	Restaurant_name=models.CharField(max_length=200,default="")
	Manager_name=models.CharField(max_length=200,default="")
	Staff_count=models.IntegerField(default=10)
	Restaurantarea=models.CharField(max_length=200,default="")
	Country=models.CharField(max_length=200,default="")
	State=models.CharField(max_length=200,default="")
	City=models.CharField(max_length=200,default="")
	Postal_code=models.IntegerField(default=10)
	Farmer_name=models.CharField(max_length=200,default="")
	Farm_size=models.IntegerField(default=10)
	Pass_book_no=models.IntegerField(default=10)
	Village=models.CharField(max_length=200,default="")
	# role = models.IntegerField(default=3,choices=t)
	# gender=models.CharField(max_length=10)
	# age=models.IntegerField(default=10)
	
	# impf=models.ImageField(upload_to='profiles/',default="profile.jpg")

	# address=models.CharField(max_length=200,default="Tirupathi")

class ExtPro(models.Model):
	is_farmer = models.BooleanField(default=False)
	age = models.IntegerField(default=10)
	mobile_number=models.CharField(max_length=12,default="")
	impf=models.ImageField(upload_to='pro/',default="user logo.png")
	address=models.CharField(max_length=100,default="")
	u = models.OneToOneField(User,on_delete=models.CASCADE)


@receiver(post_save,sender=User)
def createpf(sender,instance,created,**kwargs):
	if created:
		ExtPro.objects.create(u=instance)


class Vegpro(models.Model):
	v = [('vegetables',"Vegetables"),('Fruits','Fruits')]
	item_type=models.CharField(max_length=10,choices=v)
	item_name=models.CharField(max_length=20)
	quantity=models.IntegerField(default="")
	is_farmer = models.IntegerField(default=0)
	is_stock = models.IntegerField(default=0)
	price=models.DecimalField(max_digits=6,decimal_places=2)
	impf=models.ImageField(upload_to='images/')
	create_date=models.DateField(auto_now_add=True)
	a=models.ForeignKey(User,on_delete=models.CASCADE)

class UserPro(models.Model):
	farmers_name=models.CharField(max_length=10)
	item_type=models.CharField(max_length=10)
	item_name=models.CharField(max_length=20)
	quantity=models.IntegerField(default="")
	price=models.DecimalField(max_digits=6,decimal_places=2)
	is_status=models.IntegerField(default=0)
	e=models.ForeignKey(Vegpro,on_delete=models.CASCADE)

class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	veg=models.ForeignKey(Vegpro,on_delete=models.CASCADE)

class Myorders(models.Model):
	item_name=models.CharField(max_length=300)
	item_type=models.CharField(max_length=300)
	price=models.IntegerField()
	is_status=models.IntegerField(default=0)
	date=models.DateTimeField(auto_now_add='True',null='True')
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
