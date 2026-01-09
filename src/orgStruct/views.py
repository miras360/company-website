from django.shortcuts import render
from .models import OrgStruct, Departments

def orgStruct(request):
    file = OrgStruct.objects.order_by('-id').first()  # как и было (последний загруженный)
    departments = Departments.objects.order_by('sort_order', 'id')

    deps_list = []
    for dep in departments:
        deps_list.append({
            'name': dep.name,
            'info': dep.info.split('\n') if dep.info else []
        })

    return render(request, 'orgStructure/orgStruct.html', {'file': file, 'deps': deps_list})
