from django.contrib.auth.models import User,AbstractUser
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from FarMeKart.models import Vegpro
from FarMeKart.models import UserPro
from django.contrib.auth import get_user_model

User = get_user_model()

class UsregFo(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ['username',"email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Email",
			}),
		}
class Usperm(forms.ModelForm):
	class Meta:
		model = User
		fields=["username","role","email","proof_type"]
		widgets={
		 "username":forms.TextInput(attrs={"class":"form-control","readOnly":True,}),
		  "email":forms.EmailInput(attrs={"class":"form-control","readOnly":True,}),
		 "role":forms.Select(attrs={"class":"form-control"}),
		 "proof_type":forms.Select(attrs={"class":"form-control"})
		}
class UpdPfle1(forms.ModelForm):
	class Meta:
		model = User
		fields=["Farmer_name","Farm_size","Pass_book_no","Country","State","Village","Postal_code","impf"]
		widgets={
		 "Farmer_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Farmer_name",}),
		 "Farm_size":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Farm_size",
			}),
		 "Pass_book_no":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Pass_book_no",
			}),
		 "Country":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Country",}),
		 "State":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter State",}),
		 "Village":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Village",}),
		 "Postal_code":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Postal_code",
			}),
		}
class UpdPfle2(forms.ModelForm):
	class Meta:
		model = User
		fields=["State","Country","Postal_code","impf"]
		widgets={
		 # "Restaurant_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Restaurant_name",}),
		 # "Manager_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Manager_name",}),
		 # "Staff_count":forms.NumberInput(attrs={
			# "class":"form-control",
			# "placeholder":"Enter Staff_count",
			# }),
		 "Country":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Country",}),
		 "State":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter State",}),
		 "Postal_code":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Postal_code",
			}),

		}


class UpdPfle(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"readonly":True,
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Update EmailId",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Last Name",
			}),
		}

class ChpwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Old Password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"New Password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))
		
	class Meta:
		model=['oldpassword','newpassword','confirmpassword']

class Vegfr(forms.ModelForm):
	class Meta:
		model = Vegpro
		fields = ["item_type","item_name","quantity","price","impf"]
		widgets={
		"quantity":forms.NumberInput(attrs={
			"class":"form-control",
			"max":"500",
			"min":"150",

			})
		}



class UpdVgtab(forms.ModelForm):
	class Meta:
		model = Vegpro
		fields = ["item_type","item_name","quantity","price","is_stock","impf"]
		widgets = {
		"item_type":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"Select your Item",
			}),
		"item_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Item Name",
			}),
		"quantity":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Quantity u have",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Your Rate",
			}),
		"is_stock":forms.NumberInput(attrs={
			"class":"form-control",
			}),
		}

class Userp(forms.ModelForm):
	class Meta:
		model = UserPro
		fields=["farmers_name","item_type","item_name","quantity","price","is_status"]



