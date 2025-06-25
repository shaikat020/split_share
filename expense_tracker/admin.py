from django.contrib import admin

# Register your models here.

# tracker/admin.py
from django.contrib import admin
from .models import ExpenseSession, ExpenseEntry

admin.site.register(ExpenseSession)
admin.site.register(ExpenseEntry)
