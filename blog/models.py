from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Book(models.Model):
    objects = None
    author_name = models.CharField(max_length=80)
    book_title = models.CharField(max_length=180)

    def __str__(self):
        return self.book_title


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    book_reference = models.ForeignKey(Book, on_delete=models.CASCADE, blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Student(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    father_name = models.CharField(max_length=100)
    class_study = models.IntegerField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False, null=False)
    class_assign = models.IntegerField()

    def __str__(self):
        return self.name