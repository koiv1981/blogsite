from django.urls import path

from .views import *

urlpatterns = [
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('search', Search.as_view(), name='search'),
    path('add-subscribe', add_subscribe, name='add_subscribe'),
    path('comment/add-comment', AddComment.as_view(), name='add_comment'),
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name='logout'),
    path('', Home.as_view(), name='home'),
]
