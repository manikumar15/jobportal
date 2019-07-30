from django.contrib import admin
from .models import Search,Register,login,applyjob


# Register your models here.

class Searchadmin(admin.ModelAdmin):
    list_display = ('job','skills','experience','contact','location')
admin.site.register(Search,Searchadmin)


class Registeradmin(admin.ModelAdmin):
    list_display = ('name','email','phone','location','job','cv')
admin.site.register(Register,Registeradmin)

class loginadmin(admin.ModelAdmin):
    list_display = ('username','password','email')
admin.site.register(login,loginadmin)

class applyjobadmin(admin.ModelAdmin):
    list_display = ('fullname','email','message','cv')
admin.site.register(applyjob,applyjobadmin)
