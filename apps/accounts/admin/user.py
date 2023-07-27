# builtin imports
from django.contrib import admin

# local imports
from ..models import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "uuid")