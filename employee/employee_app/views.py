from django.shortcuts import redirect, render
from .models import UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import MyForm, MyUpdateForm
from .serializer import EmployeeeSerializer
from django.views.decorators.http import require_http_methods


# Create your views here.
class EmployeeAPI(APIView):
    def get(self, request, id = None):
        if not id:
            form = MyForm()
            return render(request, '../templates/my_template.html', {'form': form})
        else:
            employee = UserProfile.objects.get(pk=id)
            form_data = {
                'id':employee.id,
                'name': employee.name,
                'email': employee.email,
                'photo': employee.photo
                # Include other form fields as needed
            }
            form = MyUpdateForm(data=form_data)
            return render(request, '../templates/update.html', {'form': form, 'id': employee.id})
    def post(self, request):
        serializer = EmployeeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/list')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        UserProfile.objects.filter(email = request.data.get('email')).delete()
        return Response(status=status.HTTP_200_OK)
    
class ListAPI(APIView):
    def get(self, request):
        employees = UserProfile.objects.all()
        return render(request, '../templates/list.html', {'employees': employees})
    def put(self, request):
        employee_id = request.data.get('id')
        try:
            employee = UserProfile.objects.get(pk=employee_id)
            serializer = EmployeeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            pass
        return Response(status=status.HTTP_200_OK)
    
    