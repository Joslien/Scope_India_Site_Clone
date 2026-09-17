from django.contrib import admin
from .models import Category,Courses,Registration,contactdetails
# Register your models here.

admin.site.register(Category)
admin.site.register(Courses)
admin.site.register(Registration)
admin.site.register(contactdetails)
# admin.site.register(first_login)


