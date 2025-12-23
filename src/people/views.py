from django.shortcuts import render
from .models import *
# Create your views here.
def people_list(request):
    posts = People.objects.order_by('id')
    print('people : ', posts)
    return render(request, 'people/NIIPeople.html', {'people':posts})

def doctor_list(request):
    posts = Doctors.objects.order_by('id')
    datas_list = [
        {
            'photo': p.photo,
            'title': p.title,
            'content': (p.content or "").splitlines(),
        }
        for p in posts
    ]
    return render(request, 'people/doctors.html', {'datas_list': datas_list})


def teacher_list(request):
    posts = Teachers.objects.order_by('id')
    datas_list = [
        {
            'photo': p.photo,
            'title': p.title,
            'content': (p.content or "").splitlines(),
        }
        for p in posts
    ]
    return render(request, 'people/teachers.html', {'datas_list': datas_list})

def people_detail(request, pid):
    post = People.objects.get(id = pid)
    return render(request, 'people/people_detail.html', {'person':post})

# def people_new(request):
#     if request.method != 'POST':
#         form = PostForm()
#     else:
#         form = PostForm(request.POST)
#         att = request.FILES.getlist('images')
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             for image in att:
#                 PostAttachment.objects.create(
#                     file = image,
#                     post_id = post.pk
#                 )
#             return redirect('new_detail', pid=post.pk)
#     return render(request, 'posts/post_new.html', {'form':form})


