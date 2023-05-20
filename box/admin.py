from django.contrib import admin
from .models import Box, Income, TakenMoney, Info, Customer
# Register your models here.x
admin.site.register(Box)
admin.site.register(Income)
admin.site.register(TakenMoney)
admin.site.register(Info)
admin.site.register(Customer)