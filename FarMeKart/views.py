from django.shortcuts import render,redirect
from FarMeKart.forms import UsregFo,ChpwdForm,UpdPfle,Vegfr,UpdVgtab,Userp,Usperm,UpdPfle1,UpdPfle2
from django.contrib.auth.decorators import login_required
from farmer import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User,AbstractUser
from FarMeKart.models import Vegpro,User,Cart,Myorders
import sys

# Create your views here.






def remove(request,id):
	c=Cart.objects.get(id=id)
	c.delete()
	return redirect('/cartdetails')
def veg(re):
	i = Vegpro.objects.filter(a_id=re.user.id)
	s = Vegpro.objects.all()
	k = {}
	for m in s:
		g = User.objects.get(id=m.a_id)
		k[m.id] = m.item_type,m.item_name,m.quantity,m.price,m.impf,m.is_stock,m.create_date,g.username
	f = k.values()
	return render(re,'html/veg.html',{'it':i,'d':f})
	
def home(re):
	i = Vegpro.objects.filter(a_id=re.user.id)
	s = Vegpro.objects.all()
	k = {}
	for m in s:
		g = User.objects.get(id=m.a_id)
		k[m.id] = m.item_type,m.item_name,m.quantity,m.price,m.impf,m.is_stock,m.create_date,g.username
	f = k.values()
	return render(re,'html/cart1.html',{'it':i,'d':f})
	
# def home(re):
# 	return render(re,"html/home.html")
def contact(re):
	return render(re,"html/contact.html")

def about(re):
	return render(re,"html/about.html")

def registration(request):
	if request.method=="POST":
		k = UsregFo(request.POST)
		if k.is_valid():
			e = k.save(commit=False)
			sb = "Testing Email For FarMeKart"
			mg = "Hi Welcome{}. You have successfully registered for FarMeKart portal.".format(e.username)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[e.email])
			if snt == 1:
				e.save()
				return redirect('/lg')
			else:
				return redirect('/')
	k=UsregFo()
	return render(request,'html/register.html',{'h':k})

@login_required
def cgf(re):
	if re.method=="POST":
		c=ChpwdForm(user=re.user,data=re.POST)
		if c.is_valid():
			c.save()
			return redirect('lg/')
	c=ChpwdForm(user=re.user)
	return render(re,'html/changepassword.html',{'t':c})

@login_required
def profile(req):
	return render(req,'html/profile.html')

@login_required
def updprofile(request):
	if request.method == "POST":
		t = UpdPfle(request.POST,instance=request.user)
		if t.is_valid():
			t.save()
			return redirect('/pro')
	t = UpdPfle(instance=request.user)
	return render(request,'html/updateprofile.html',{'z':t})


@login_required
def dashboard(re):
	return render(re,'html/dashboard.html')

@login_required
def farmerdashboard(request):
	return render(request,'html/farmerdashboard.html')


@login_required
def vegf(request):
	t = Vegpro.objects.filter(a_id=request.user.id)
	if request.method == "POST":
		s = Vegfr(request.POST,request.FILES)
		if s.is_valid():
			r = s.save(commit=False)
			r.a_id = request.user.id
			r.save()
			return redirect('/dt')
	s=Vegfr()
	return render(request,'html/data.html',{'a':s,'e':t})




@login_required
def infodelete(req,et):
	data=Vegpro.objects.get(id=et)
	print(data.id)
	if req.method == "POST":
		print(data.id)
		data.delete()
		return redirect('/dt')
	return render(req,'html/userdelete.html',{'sd':data})

def itemupdate(request,y):
	dc = Vegpro.objects.get(id=y)
	if request.method == "POST":
		m = UpdVgtab(request.POST,request.FILES,instance=dc)
		if m.is_valid():
			m.save()
			return redirect('/dt')
	m = UpdVgtab(instance=dc)
	return render(request,'html/updateuser.html',{'e':m})





@login_required
def items(request):
	i = Vegpro.objects.filter(a_id=request.user.id)
	data=Vegpro.objects.all()
	for j in i:
		print(j.item_name)
	s = Vegpro.objects.all()
	k = {}
	for m in s:
		g = User.objects.get(id=m.a_id)
		k[m.id] = m.item_type,m.item_name,m.quantity,m.price,m.impf,m.is_stock,m.create_date,g.username
	f = k.values()
	return render(request,'html/cart.html',{'data':data,'d':f})

def addcart(request,id):
	r=Vegpro.objects.get(id=id)
	if request.method == 'POST':
		p=Cart(user_id=request.user.id,veg_id=id)
		p.save()
		
		return redirect("/cartdetails")
	
	return render(request,'html/cart.html',{'data':r})

def usr(re):
	s=Userp()
	return render(re,'html/user.html',{'a':s})
def requestform(rq):
	e2=User.objects.get(id=rq.user.id)
	if rq.method=='POST':
		print(e2)
		e2.age=rq.POST['age']
		e2.impf=rq.FILES['fil']
		e2.address=rq.POST['ad']
		e2.save()
		return redirect('/lg')
	k2= Usperm(instance=e2)
	return render(rq,'html/requestp.html',{'y':k2})


def adminpermissions(request):
	ty=User.objects.all()
	return render(request,'html/adminpermissions.html',{'q':ty})
def updatepermissions(request,k):
	r=User.objects.get(id=k)
	if request.method == "POST":
		k=Usperm(request.POST,instance=r)
		if k.is_valid():
			k.save()
			return redirect('/gper')
	k2= Usperm(instance=r)
	return render(request,'html/updatepermissions.html',{'y':k2})

def updateprofile(request):
	return render(request,'html/profileupdate.html')

def orgupdate(request):
	z=User.objects.get(id=request.user.id)
	if request.method == "POST":
		p=UpdPfle1(request.POST,instance=z)
		q=UpdPfle2(request.POST,instance=z)
		r=UpdPfle(request.POST,instance=z)
		if p.is_valid() and q.is_valid() and r.is_valid():
			p.save()
			q.save()
			r.save()
			return redirect('/profile')
	p=UpdPfle1(instance=z)
	q=UpdPfle2(instance=z)
	r=UpdPfle(instance=z)
	return render(request,'html/updatedetails.html',{'u':p,'p':q,'k':r})

def userdelete(request,id):
	c=User.objects.get(id=id)
	c.delete()
	c.save()
	return redirect('/gper')

def addcart(request,id):
	b=Vegpro.objects.get(id=id)
	print("hi")
	print(b)

	c=Cart(user_id=request.user.id,veg_id=id)
	c.save()
	count=0
	data1 = Cart.objects.filter(user_id=request.user.id)
	for i in data1:
		count+=1
	return render(request,'html/addcart.html',{'b':c,'count':count,'data1':data1})

def cartdetails(request):
	c=Cart.objects.filter(user_id=request.user.id)
	sum=0
	count=0
	for i in c:
		count=count+1
		sum=sum+i.veg.price
	return render(request,'html/cartdetails.html',{'sum':sum,'count':count,'cart':c})

def placeorder(request):
	c=Cart.objects.filter(user_id=request.user.id)
	sum=0
	count=0
	for i in c:
		count=count+1
		sum=sum+i.veg.price
		return render(request,'html/placeorder.html',{'sum':sum,'count':count,'cart':c})

def msg(request):
	c=Cart.objects.filter(user_id=request.user.id)
	sum=0
	count=0
	for i in c:
		count=count+1
		sum=sum+i.veg.price
	return render(request,'html/message.html',{'count':count})


def msg1(request):
	c=Cart.objects.filter(user_id=request.user.id)
	sum=0
	count=0
	for i in c:
		count=count+1
		sum=sum+i.veg.price
	return render(request,'html/message1.html',{'count':count})


def myorders(request):
	my=Myorders.objects.filter(user_id=request.user.id)
	sum=0
	count=0
	for i in my:
		count=count+1
		sum=sum+i.price
	return render(request,'html/myorders.html',{'sum':sum,'my':my})

def checkout(request):
	c=Cart.objects.filter(user_id=request.user.id)
	if request.method=="POST":
		for i in c:
			sum=sum+i.veg.price
			for i in c:
				sum=sum+i.veg.price
				a=Myorders(item_name=i.veg.item_name,price=i.veg.price,user_id=request.user.id)
				a.save()
				he=Product.objects.filter(id=i.veg_id)
				for i in he:
					c.delete()
			return redirect('msg')
		return redirect('msg1')
	return render(request,'html/placeorder.html')


	




