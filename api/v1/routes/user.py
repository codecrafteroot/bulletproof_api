# builtin imports
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# local imports
from ..viewsets import UserViewSet

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = format_suffix_patterns([
    path('users/', user_list, name='user_list'),
    path('users/<int:pk>/', user_detail, name='user_detail')
])