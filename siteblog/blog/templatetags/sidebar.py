from django import template
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
