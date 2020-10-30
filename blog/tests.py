import json
from django.test import TestCase
import unittest
from .models import Book, Student
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class BookAPIStatusCodeTestCase(APITestCase):
    # On book create it return the status code 201
    def test_create_book(self):
        url = reverse('book-list')
        data = {'author_name': 'R.K Sharma', 'book_title': 'Learn English'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().author_name, 'R.K Sharma')


class BookEndPointTestCase(APITestCase):
    def setUp(self):
        Book.objects.create(author_name="M Gupta", book_title="Let us c")

    # create Book data and return the status code 200
    def test_check_endpoint(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class StudentFilterTestCase(TestCase):
    def setUp(self):
        Student.objects.create(name="dharam2", roll_no=15, father_name="davinder2", class_study=12)

    # Check Query set of Student Model
    def test_student_filter(self):
        self.assertEqual(Student.objects.filter(name="dharam2").exists(),True)


class StudentEndPointTestCase(APITestCase):
    def setUp(self):
        Student.objects.create(name="dharam", roll_no=14, father_name="davinder", class_study=12)

    def test_student_list(self):
        # Check Query set for student_list of Student Model
        response = self.client.get(reverse("student-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_detail(self):
        # Check Query set for student_detail of Student Model
        response = self.client.get(reverse("student-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'name': 'dharam', 'roll_no': 14, 'father_name': "davinder", 'class_study': 12})

    def test_student_patch(self):
        # Check Query set for student_patch of Student Model
        data = {"name":"dharam3"}
        response = self.client.patch(reverse('student-detail', kwargs={"pk": 1}),data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_delete(self):
        # Check Query set for student_delete of Student Model
        response = self.client.delete(reverse('student-detail', kwargs={"pk": 1}), format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(author_name="M Gupta", book_title="Let us c")
        Book.objects.create(author_name="R.K Sharma", book_title="Learn English")

    def test_book_name_title(self):
        book1 = Book.objects.get(author_name="M Gupta", book_title="Let us c")
        book2 = Book.objects.get(author_name="R.K Sharma", book_title="Learn English")
        # Test that the name and title of the book model match
        self.assertEqual(book1.author_name, "M Gupta")
        self.assertEqual(book1.book_title, "Let us c")
        self.assertEqual(book2.author_name, "R.K Sharma")
        self.assertEqual(book2.book_title, "Learn English")


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(name="kiran", roll_no=40, father_name="mandeep", class_study=8)
        Student.objects.create(name="herjot", roll_no=55, father_name="arsh", class_study=6)
        Student.objects.create(name="baldev", roll_no=60, father_name="daleep", class_study=8)
        Student.objects.create(name="karan", roll_no=62, father_name="baljit", class_study=4)

    def test_student(self):
        student_name = Student.objects.get(name="kiran", roll_no=40, father_name="mandeep", class_study=8)
        message = "student study in more than sixth class"
        # Test that the student class is greater than 6 class
        self.assertGreater(student_name.class_study, 6, message)

    def test_student_instance(self):
        student_name = Student.objects.get(name="kiran", roll_no=40, father_name="mandeep", class_study=8)
        # Test that the student name is instance of string data type
        self.assertIsInstance(student_name.name, str)

    # def test_list_CountEqual(self):
    #     list1 = [1, 2, 3, 4]
    #     list2 = [1, 2, 3, 4]
    #     # Test that the list1 and list2 count equal data
    #     self.assertCountEqual(list1, list2)


if __name__ == '__main__':
    unittest.main()
