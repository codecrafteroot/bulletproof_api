# builtin imports
from django.contrib import admin

# local imports
from ..models import UserModel
from ..forms import UserCreationForm, UserChangeForm

class UserAdmin(admin.ModelAdmin):
    model = UserModel
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ("email", "username", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)