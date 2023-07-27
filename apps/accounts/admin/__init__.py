# builtin imports
from django.contrib import admin

# local imports
from .user import UserAdmin
from ..models import UserModel

admin.site.register(UserModel, UserAdmin)