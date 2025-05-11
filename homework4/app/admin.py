from django.contrib import admin
from app.models.student import Student
from app.models.department import Department
from app.models.position import Position


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    search_fields = ("name",)
    list_filter = ("name",)
    list_per_page = 10
    ordering = ("id",)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_active",
        "department",
    )
    search_fields = ("name",)
    list_filter = ("is_active", "department")
    list_per_page = 10
    ordering = ("id",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone_number",
    )
    search_fields = ("first_name", "last_name")
    list_filter = ("course",)
    list_per_page = 10
    ordering = ("id",)
