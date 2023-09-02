from django.contrib import admin
from .models import User,Profile,Note
# Register your models here.

class UserAdmin(admin.ModelAdmin):
     readonly_fields = ['password']

admin.site.register(User,UserAdmin)
admin.site.register(Profile)
admin.site.register(Note)
