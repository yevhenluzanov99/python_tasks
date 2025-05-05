from django.contrib import admin
from app.models.student import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone_number",
    )  # адаптуйте під свої поля
    search_fields = ("first_name", "last_name")
    list_filter = ("course",)
    list_per_page = 10
    ordering = ("id",)
