from django.contrib import admin
from .models import Business_Basic_Info, Business_Condition, Cashflow, Balance_sheet

# Register your models here.
admin.site.register(Business_Basic_Info)
admin.site.register(Business_Condition)
admin.site.register(Cashflow)
admin.site.register(Balance_sheet)
