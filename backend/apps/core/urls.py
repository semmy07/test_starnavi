from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from apps.core.views import RegistrationAPIView, PostEndpoint

urlpatterns = [
    path('auth-jwt/', obtain_jwt_token),
    path('auth-jwt-refresh/', refresh_jwt_token),

    path('registration/', RegistrationAPIView.as_view()),
    path('post-endpoint/', PostEndpoint.as_view())
]
