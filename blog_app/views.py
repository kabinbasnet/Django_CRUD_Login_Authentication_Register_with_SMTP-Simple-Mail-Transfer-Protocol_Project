from blog_app.forms import AddBlogsNews
from blog_app.models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
# Create your views here.


@login_required
def home(request):
    form = Blog.objects.all()
    return render(request, 'home.html', {'form': form})


@login_required
def add(request):
    if request.method == 'GET':
        form = AddBlogsNews()
        return render(request, 'add_blog.html', {'form': form})
    else:
        form = AddBlogsNews(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            Blog.objects.create(title=title, content=content,
                                author_id=request.user.id)
            return redirect('home')
        else:
            return render(request, 'add_blog.html', {'form': form})


@login_required
def delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()

    return redirect('home')


@login_required
def edit(request, id):
    try:
        blog = Blog.objects.get(id=id)

    except Blog.DoesNotExist:
        # Note: if there is an error,then, this code will be executed.
        messages.error(request, 'Blog doesnot exist')
        return redirect('error')

    else:
        # Note: if there is no any error,then, this code will be executed.
        if request.method == 'GET':
            form = AddBlogsNews(instance=blog)
            return render(request, 'edit_blog.html', {'form': form})
        else:
            form = AddBlogsNews(request.POST, instance=blog)
            if form.is_valid:
                form.save()
                return redirect('home')
            else:
                return render(request, 'edit_blog.html', {'form': form})


def error(request):
    return render(request, 'error.html')
