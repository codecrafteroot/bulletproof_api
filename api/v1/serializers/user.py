# builtin imports
from rest_framework.serializers import ModelSerializer

# local imports
from apps.accounts.models import UserModel

# Serializers define the API representation.

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'