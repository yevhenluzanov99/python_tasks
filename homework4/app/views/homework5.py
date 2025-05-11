from django.http import JsonResponse
from django.db.models import Q
from app.models.department import Department
from app.models.position import Position


def homework_querysets(request):
    """
    Запит 1: Знайдіть усі відділи (Department), у яких є позиції менеджерів,
    та впорядкуйте їх за назвою відділу в алфавітному порядку.
    Використовуйте filter() і order_by().
    """
    departments_with_managers = (
        Department.objects.filter(position__name__icontains="менеджер")
        .order_by("name")
        .distinct()
    )
    """
    Запит 2: Знайдіть загальну кількість активних позицій (Position). 
    Використовуйте filter() та count().
    """
    active_positions_count = Position.objects.filter(is_active=True).count()
    """
    Запит 3: Виберіть усі позиції, які є активними або які належать до відділу з назвою "HR". 
    Використовуйте filter() і OR (|).
    """
    active_or_hr_positions = Position.objects.filter(
        Q(is_active=True) | Q(department__name="HR")
    )
    """
    Запит 4: Виберіть назви всіх відділів (Department), в яких є менеджери. 
    Використовуйте filter() та values().
    """
    departments_with_managers_names = (
        Department.objects.filter(position__name__icontains="менеджер")
        .values("name")
        .distinct()
    )
    """
    Запит 5: Виберіть усі позиції, відсортовані за назвою, 
    але виводьте лише назву та інформацію про активність.
    Використовуйте order_by() і values().
    """
    positions_sorted = Position.objects.order_by("name").values("name", "is_active")

    data = {
        "departments_with_managers": list(
            departments_with_managers.values("id", "name")
        ),
        "active_positions_count": active_positions_count,
        "active_or_hr_positions": list(active_or_hr_positions.values("id", "name")),
        "departments_with_managers_names": list(departments_with_managers_names),
        "positions_sorted": list(positions_sorted),
    }

    return JsonResponse(data, json_dumps_params={"ensure_ascii": False})
