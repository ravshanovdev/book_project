from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import UserSerializer, GetUserSerializer, EmployeeSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth import get_user_model
from .models import Employee
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import FormParser, MultiPartParser
User = get_user_model()


class RegisterApiView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['accounts'],
        request_body=UserSerializer,
        responses={201: "User created"}
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    @swagger_auto_schema(
        tags=["accounts"],
        operation_summary="get_all_users"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class GetAllUsers(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=["accounts"],
        operation_summary="get_all_users"
    )
    def get(self, request):
        users = User.objects.all()
        serializer = GetUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Employee API Views

class AddEmployeeAPIView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [FormParser, MultiPartParser]


    @swagger_auto_schema(
        tags=['employee'],
        request_body=EmployeeSerializer,
        responses={
            201: f"{EmployeeSerializer}",
            400: 'Bad Request'
        }
    )
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmployeeListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    @swagger_auto_schema(
        tags=['employee']
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class EmployeeDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    @swagger_auto_schema(
        tags=['employee']
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UpdateEmployeeAPIView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [FormParser, MultiPartParser]

    @swagger_auto_schema(
        tags=['employee'],
        request_body=EmployeeSerializer,
        responses={
            200: f"{EmployeeSerializer}",
            400: 'Bad Request',
            404: 'Not Found'
        }
    )
    def patch(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class EmployeeDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['employee'],
        operation_summary="delete_employee"
    )
    def delete(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found."}, status=status.HTTP_404_NOT_FOUND)

        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









