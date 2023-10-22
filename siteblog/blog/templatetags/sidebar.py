from django import template
from django.db.models import Max

from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('blog/popular_post_tpl.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {"posts": posts}


@register.inclusion_tag('blog/get_tag_tpl.html')
def get_tag():
    tags = Tag.objects.all()
    return {"tags": tags}


@register.inclusion_tag('blog/most_popular_post_tpl.html')
def max_views():
    a = Post.objects.aggregate(max_v=Max('views'))
    post = Post.objects.get(views=a.get('max_v'))
    return {"post": post}
