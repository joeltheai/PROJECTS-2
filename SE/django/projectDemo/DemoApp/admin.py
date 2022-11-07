from django.contrib import admin

# Register your models here.
from .models import bankDetails
admin.site.register(bankDetails)

from .models import bankAccount
admin.site.register(bankAccount)
