from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListAPI.as_view(), name='home_api'),
    path('employee_api', views.EmployeeAPI.as_view(), name='employee_api'),
    path('employee_api/<int:id>', views.EmployeeAPI.as_view(), name='employee_api_with_id'),
    path('list', views.ListAPI.as_view(), name='employee_list_api'),
]