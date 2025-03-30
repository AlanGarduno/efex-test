from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from student.models import Student
from student.serializers import StudentSerializer
from student.tests.student_faker import create_fake_student, create_fake_student_payload


class TestStudentViewSet(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_all_students(self):
        fake_students = [create_fake_student() for _ in range(5)]
        url = reverse('student:student-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        fake_students.sort(key=lambda x: x.id)
        expected_data = StudentSerializer(
            fake_students,
            many=True
        ).data
        self.assertEqual(response.json(), expected_data)

    def test_get_student_by_id(self):
        fake_student = create_fake_student()
        url = reverse('student:student-detail', args=[fake_student.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = StudentSerializer(fake_student).data
        self.assertEqual(response.json(), expected_data)

    def test_get_student_by_id_404(self):
        url = reverse('student:student-detail', args=[100])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_student(self):
        url = reverse('student:student-list')
        payload = create_fake_student_payload()
        res = self.client.post(url, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        student_id = res.json().get('id')
        student = Student.objects.get(id=student_id)
        for k, v in payload.items():
            self.assertEqual(getattr(student, k), v)

    def test_update_student(self):
        fake_student = create_fake_student()
        url = reverse('student:student-detail', args=[fake_student.id])
        payload = create_fake_student_payload()
        res = self.client.patch(url, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_student_404(self):
        url = reverse('student:student-detail', args=[100])
        payload = create_fake_student_payload()
        res = self.client.patch(url, payload)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
