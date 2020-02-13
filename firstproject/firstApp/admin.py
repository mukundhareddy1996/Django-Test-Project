from django.contrib import admin
from firstApp.models import employee


class employeeAdmin(admin.ModelAdmin):
    list_display = ['id','Name','email']

# Register your models here.
admin.site.register(employee,employeeAdmin)