from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from ..models import UserModel


class UserCreationForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = ("email",)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = UserModel
        fields = ("email",)