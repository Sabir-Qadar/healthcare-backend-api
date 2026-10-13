
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views import (
    RegisterView,
    PatientListCreateView,
    PatientDetailView,
)
from api.serializers import EmailTokenObtainPairSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/auth/register/", RegisterView.as_view(), name="register"),
    path("api/auth/login/", EmailTokenObtainPairView.as_view(), name="login"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("api/patients/", PatientListCreateView.as_view(), name="patient-list-create"),
    path("api/patients/<int:pk>/", PatientDetailView.as_view(), name="patient-detail"),
]
