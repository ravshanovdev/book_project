from django.urls import path
from .views import (RegisterApiView, CustomTokenObtainPairView, GetAllUsers, EmployeeListAPIView, EmployeeDetailAPIView,
                    AddEmployeeAPIView, EmployeeDeleteAPIView, UpdateEmployeeAPIView)
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'), # tested
    path('login/', CustomTokenObtainPairView.as_view(), name='login'), # tested
    path('refresh-token/', TokenRefreshView.as_view(), ),

    path('add_employee/', AddEmployeeAPIView.as_view(), name='add-employee'), # tested
    path('update_employee/<int:pk>/', UpdateEmployeeAPIView.as_view(), name='update-employee'), # tested
    path('get_all_employees/', EmployeeListAPIView.as_view(), name='employee-list'), # tested
    path('get_employee/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee-detail'), # tested
    path('delete_employee/<int:pk>/', EmployeeDeleteAPIView.as_view(), name='employee-delete'), # tested


    path('get_all_user/', GetAllUsers.as_view(), ),

]