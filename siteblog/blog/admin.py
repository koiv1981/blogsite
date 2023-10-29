from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.utils.safestring import mark_safe


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title",)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title",)


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "created_at", "views", "category", "get_photo", "views")
    list_display_links = ("title", "category")
    readonly_fields = ("views", "created_at", "get_photo")
    search_fields = ("title",)
    list_filter = ("category", "tags")
    save_as = True
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return "Фото отсутствует"

    get_photo.__name__ = "Миниатюра"


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    readonly_fields = ("email", "created_at")
    list_filter = ("created_at",)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "content", "created_at", "updated_at", "is_published")
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("created_at", "is_published")
    search_fields = ("name", "email", "content")
    save_as = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Subscriber, SubscribeAdmin)
admin.site.register(Comment, CommentAdmin)
