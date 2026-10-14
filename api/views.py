
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Patient,Doctor, PatientDoctorMapping
from .serializers import RegisterSerializer, PatientSerializer,DoctorSerializer,PatientDoctorMappingSerializer
from rest_framework.response import Response



class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

class PatientDoctorMappingListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__user=self.request.user
        )


class PatientDoctorMappingByPatientView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__user=self.request.user,
            patient_id=self.kwargs["patient_id"]
        )




class PatientDoctorMappingDetailView(generics.GenericAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__user=self.request.user
        )

    def get(self, request, pk):
        mappings = self.get_queryset().filter(patient_id=pk)
        serializer = self.get_serializer(mappings, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        mapping = self.get_queryset().filter(pk=pk).first()

        if mapping is None:
            from rest_framework.exceptions import NotFound
            raise NotFound("Mapping not found.")

        mapping.delete()
        return Response(status=204)
