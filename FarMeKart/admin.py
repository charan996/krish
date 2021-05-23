from django.contrib import admin
from FarMeKart.models import ExtPro,Vegpro,User,Myorders,Cart
# Register your models here.
admin.site.register(User)
admin.site.register(ExtPro)
admin.site.register(Vegpro)
admin.site.register(Cart)
admin.site.register(Myorders)
