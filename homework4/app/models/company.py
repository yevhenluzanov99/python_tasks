from django.db import models
from django.core.exceptions import ValidationError


class Company(models.Model):
    class Meta:
        db_table = "company"

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    tax_code = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.pk and Company.objects.exists():
            raise ValidationError("There can be only one Company instance.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
