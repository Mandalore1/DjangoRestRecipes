from django.contrib import admin

# Register your models here.
from users.models import UserAdditionalInfo

admin.site.register(UserAdditionalInfo)
