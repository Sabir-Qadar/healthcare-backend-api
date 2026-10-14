
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
    DoctorListCreateView,
    DoctorDetailView,
    PatientDoctorMappingListCreateView,
    PatientDoctorMappingByPatientView,
    PatientDoctorMappingDetailView,
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
    path("api/doctors/", DoctorListCreateView.as_view(), name="doctor-list-create"),
    path("api/doctors/<int:pk>/", DoctorDetailView.as_view(), name="doctor-detail"),
    
   path(
        "api/mappings/",
        PatientDoctorMappingListCreateView.as_view(),
        name="mapping-list-create",
    ),
   path(
        "api/mappings/patient/<int:patient_id>/",
        PatientDoctorMappingByPatientView.as_view(),
        name="mapping-by-patient",
    ),
    path(
        "api/mappings/<int:pk>/",
        PatientDoctorMappingDetailView.as_view(),
        name="mapping-detail",
    ),

]
