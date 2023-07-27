# builtin imports
from django.urls import path, include

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('accounts/', include('apps.accounts.urls')),
    path('authentication/', include('apps.authentication.urls')),
]