from django.shortcuts import get_object_or_404, render, redirect
from .models import BlogpostModel,CategoryModel
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    blogpost_objs = BlogpostModel.objects.all()
    context = {
        "blogposts":blogpost_objs
    }
    # print(blogpost_objs.image.)
    return render(request, 'home.html', context)

def category(request):
    technology= CategoryModel.objects.all().values('title','description')
    # category_objs = BlogpostModel.objects.all()
    
    context={ 
        'technology':technology
    }
    return render(request, 'category.html', context)



def blogpost_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogpost_list')
    else:
        form = BlogPostForm()
    return render(request, 'blogpost_create.html', {'form': form})

def blogpost_update(request, pk):
    post = get_object_or_404(BlogpostModel, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogpost_list')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpost_update.html', {'form': form})

def blogpost_delete(request, pk):
    post = get_object_or_404(BlogpostModel, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blogpost_list')
    return render(request, 'blogpost_delete.html', {'post': post})



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
