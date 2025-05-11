from django.db import models
from .department import Department


class Position(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
