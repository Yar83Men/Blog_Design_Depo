from django.shortcuts import render, redirect
from .forms import FeedBackForm
from .models import Posts, Category, Tags


def posts_all(request):
    posts_list = Posts.objects.all()
    categories = Category.objects.all()
    tags = Tags.objects.all()
    context = {
        'posts': posts_list,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'myapp/all_posts.html', context=context)


def sort_by_date(request):
    if request.method == 'POST':
        if request.POST['time'] == 'new':
            posts_list = Posts.objects.all().order_by('-time_create')
            categories = Category.objects.all()
            tags = Tags.objects.all()
            choice = 'cначала новые'
            context = {
                'posts': posts_list,
                'categories': categories,
                'tags': tags,
                'choice': choice

            }
            return render(request, 'myapp/all_posts.html', context=context)
        else:
            posts_list = Posts.objects.all()
            categories = Category.objects.all()
            choice = 'cначала старые'
            context = {
                'posts': posts_list,
                'categories': categories,
                'choice': choice
            }
            return render(request, 'myapp/all_posts.html', context=context)


def sort_by_category(request):
    categories = Category.objects.all()
    tags = Tags.objects.all()
    if request.method == 'POST':
        if request.POST['category']:
            sort_by_category = Posts.objects.filter(cat_id=request.POST['category'])
            category_name = Category.objects.get(pk=request.POST['category'])
            context = {
                'posts': sort_by_category,
                'categories': categories,
                'tags': tags,
                'cat_name': category_name
            }
            return render(request, 'myapp/all_posts.html', context=context)


def sort_by_tag(request):
    categories = Category.objects.all()
    tags = Tags.objects.all()
    if request.method == 'POST':
        if request.POST['tag']:
            sort_by_tag = Posts.objects.filter(tags=request.POST['tag'])
            tag_name = Tags.objects.get(pk=request.POST['tag'])
            context = {
                'posts': sort_by_tag,
                'categories': categories,
                'tags': tags,
                'tag_name': tag_name
            }
            return render(request, 'myapp/all_posts.html', context=context)


def post_detail(request, post_id):
    categories = Category.objects.all()
    tags = Tags.objects.all()
    post = Posts.objects.get(pk=post_id)
    context = {
        'posts': post,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'myapp/post_detail.html', context=context)


def feedback(request):
    form = FeedBackForm
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        'form': form
    }
    return render(request, 'myapp/feedback_form.html', context=context)