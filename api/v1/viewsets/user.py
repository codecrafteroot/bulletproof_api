# builtin imports
from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

# local imports
from apps.accounts.models import UserModel
from ..serializers import UserSerializer

# ViewSets define the view behavior.

class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = []