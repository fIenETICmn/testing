from django.contrib import admin
from .models import User, Book, Post, Student, Teacher


admin.site.register(User)
admin.site.register(Book)
admin.site.register(Post)
admin.site.register(Student)
admin.site.register(Teacher)


