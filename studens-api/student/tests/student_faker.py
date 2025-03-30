from faker import Faker

from student.models import Student

fake = Faker()

def create_fake_student():
    return Student.objects.create(
        id=fake.random_int(min=1, max=1000),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        date_of_birth=fake.date_of_birth(minimum_age=10, maximum_age=18),
        grade=fake.random_int(min=1, max=10),
        phone=fake.phone_number()[:10],
        email=fake.email())

def create_fake_student_payload():
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'date_of_birth': fake.date_of_birth(minimum_age=10, maximum_age=18),
        'grade': fake.random_int(min=1, max=10),
        'phone': fake.phone_number()[:10],
        'email': fake.email()
    }
