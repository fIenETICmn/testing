from django.shortcuts import render
from blog.models import User, Book, Post, Student, Teacher
from blog.api.serializers import UserSerializer, BookSerializer, PostSerializer, StudentSerializer, TeacherSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'books': reverse('book-list', request=request, format=format),
        'posts': reverse('posts-list', request=request, format=format),
        'students': reverse('students-list', request=request, format=format),
        'teachers': reverse('teachers-list', request=request, format=format),
    })