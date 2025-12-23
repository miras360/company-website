from django.shortcuts import render, redirect
from .models import PostCeo, PostAttachment
from .forms import PostForm
# Create your views here.

def post_list(request):
    posts = PostCeo.objects.order_by('-date')
    for post in posts:
        original = post.content or ""
        # делаем превью, но НЕ портим оригинальный content
        preview = " ".join(original.split()[:40])
        if preview != original:
            preview += " ..."
        post.preview = preview

        post.att = PostAttachment.objects.filter(post_id=post.pk)
    return render(request, 'ceoblog/blogCEO.html', {'post_list': posts})


def post_detail(request, pid):
    post = PostCeo.objects.get(id = pid)
    attachments = PostAttachment.objects.filter(post_id = pid)
    return render(request, 'ceoblog/post_detail.html', {'post':post, 'attachments': attachments})

def post_new(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        att = request.FILES.getlist('images')
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            for image in att:
                PostAttachment.objects.create(
                    file = image,
                    post_id = post.pk
                )
            return redirect('post_detail', pid=post.pk)
    return render(request, 'ceoblog/post_new.html', {'form':form})

def post_edit(request, pid):
    post = PostCeo.objects.get(pk=pid)
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
