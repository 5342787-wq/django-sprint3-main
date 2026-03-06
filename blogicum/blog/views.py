from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from blog.models import Post, Category

current_time = timezone.now()

def index(request):
    template = 'blog/index.html'
    
    posts_list = Post.objects.select_related(
        'category', 'location'
    ).filter(
        # Проверяем, что
        is_published=True,  # Сорт разрешён к публикации;
        category__is_published=True,  # Категория разрешена к публикации.
        pub_date__lte=current_time
    ).order_by('-pub_date')[:5]
    context = {'post_list': posts_list}
    return render(request, template, context)


def post_detail(request, post_id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related(
            'category', 'location'
        ).filter(is_published=True,
                 pub_date__lte=current_time,
                 category__is_published=True),
        pk=post_id
    )
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    post_list = Post.objects.select_related(
        'category', 'location'
    ).filter(is_published=True,
             category__is_published=True,
             pub_date__lte=current_time,
             category__slug=category_slug)
        # pk=category_slug
    category = get_object_or_404(Category.objects.values(
        'id', 'title', 'description'
        ).filter(is_published=True, slug=category_slug))

    context = {'post_list': post_list,
               'category': category}
    print(context)

    return render(request, template_name, context)
