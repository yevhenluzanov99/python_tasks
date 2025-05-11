from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .course import Course


class Student(models.Model):
    class Meta:
        db_table = "it_students"

    # id = models.BigAutoField()
    first_name = models.TextField(null=False)
    last_name = models.TextField(null=False)
    completed_lessons = models.IntegerField()
    birth_date = models.DateField(null=True)
    avatar = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # або як у вас вказано
