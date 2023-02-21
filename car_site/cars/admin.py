from django.contrib import admin
from .models import car
# Register your models here.
class carAdmin(admin.ModelAdmin):
    list_display = ('id','car_title','color','model')


admin.site.register(car,carAdmin)