from django.shortcuts import render, get_object_or_404
from .models import OrgStruct, Departments

def orgStruct(request):
    file = OrgStruct.objects.order_by('-id').first()
    # Передаем объекты напрямую, сохраняя сортировку
    departments = Departments.objects.all() 
    return render(request, 'orgStructure/orgStruct.html', {'file': file, 'departments': departments})

def department_detail(request, pk):
    # Извлекаем конкретное управление или отдаем 404
    department = get_object_or_404(Departments, pk=pk)
    return render(request, 'orgStructure/department_detail.html', {'department': department})