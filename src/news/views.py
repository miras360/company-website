from django.shortcuts import render, redirect
from .models import Post, PostAttachment
from .forms import PostForm
# Create your views here.

def post_list(request):
    posts = Post.objects.order_by('-date')
    post_list = []
    for post in posts:
        original_content = post.content
        post.content = ' '.join(original_content.split()[:40])
        # Если содержимое было сокращено, добавляем многоточие в конец строки
        if original_content != post.content:
            post.content += ' ...'
        att = PostAttachment.objects.filter(post_id = post.pk).first()
        post_obj = {
            'pk': post.pk if post else None,
            'author': post.author if post else None,
            'title': post.title if post else None,
            'date': post.date if post else None,
            'content': post.content if post else None,
            'att': att if att else None,
        }
        post_list.append(post_obj)
    return render(request, 'posts/post_list.html', {'post_list':post_list})

def post_detail(request, pid):
    post = Post.objects.get(pk=pid)
    attachments = PostAttachment.objects.filter(post=post)

    return render(
        request,
        'posts/post_detail.html',
        {
            'post': post,
            'attachments': attachments,
        }
    )

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        att = request.FILES.getlist('images')
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            for image in att:
                PostAttachment.objects.create(
                    file=image,
                    post=post,  # Используем пост, а не post_id
                    # type = "img",
                )
            return redirect('new_detail', pid=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_new.html', {'form': form})

def post_edit(request, pid):
    post = Post.objects.get(pk=pid)
    post_att = PostAttachment.objects.filter(post_id = post.pk)
    # print(post_att)
    if request.method != "POST":
        form = PostForm(instance=post)
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            att = request.FILES.getlist('images')
            for image in att:                   
                PostAttachment.objects.create(
                    file = image,
                    post_id = post.pk
                )
            chosen = request.POST.getlist('attachments')
            # print(chosen)
            for image_id in chosen:
                PostAttachment.objects.get(pk=int(image_id)).delete()
            post.edited = True
            post.save()
            return redirect('new_detail', pid = post.pk)
    return render(request, 'posts/post_edit.html', {'form':form, 'post_att':post_att})
