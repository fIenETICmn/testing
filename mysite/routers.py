from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog.views import *
from rest_framework.routers import DefaultRouter
from blog.api.viewset import UserViewSet, BookViewSet, PostViewSet, StudentViewSet, TeacherViewSet
from blog.api import viewset

router = DefaultRouter()

router.register(r'users', viewset.UserViewSet)
router.register(r'books', viewset.BookViewSet)
router.register(r'posts', viewset.PostViewSet)
router.register(r'students', viewset.StudentViewSet)
router.register(r'teachers', viewset.TeacherViewSet)


user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
books_list = BookViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
books_detail = BookViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
posts_list = PostViewSet.as_view({
    'get': 'list'
})
posts_detail = PostViewSet.as_view({
    'get': 'retrieve'
})
students_list = StudentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
students_detail = StudentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
teachers_list = TeacherViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
teachers_detail = TeacherViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# API endpoints
urlpatterns = format_suffix_patterns([
    # path('', api_root),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('books/', books_list, name='book-list'),
    path('books/<int:pk>/', books_detail, name='book-detail'),
    path('posts/', posts_list, name='post-list'),
    path('posts/<int:pk>/', posts_detail, name='post-detail'),
    path('students/', students_list, name='student-list'),
    path('students/<int:pk>/', students_detail, name='student-detail'),
    path('teachers/', teachers_list, name='teacher-list'),
    path('teachers/<int:pk>/', teachers_detail, name='teacher-detail'),

])
urlpatterns += router.urls