from django.urls import path
from .views import (RegisterApiView, CustomTokenObtainPairView, GetAllUsers, EmployeeListAPIView, EmployeeDetailAPIView,
                    AddEmployeeAPIView, EmployeeDeleteAPIView, UpdateEmployeeAPIView)
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), ),

    path('add_employee/', AddEmployeeAPIView.as_view(), name='add-employee'),
    path('update_employee/<int:pk>/', UpdateEmployeeAPIView.as_view(), name='update-employee'),
    path('get_all_employees/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('get_employee/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee-detail'),
    path('delete_employee/<int:pk>/', EmployeeDeleteAPIView.as_view(), name='employee-delete'),


    path('get_all_user/', GetAllUsers.as_view(), ),

]