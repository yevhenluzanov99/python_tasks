from django.db import models


class Course(models.Model):
    name = models.TextField()
    description = models.TextField()
    learning_plan = models.TextField(blank=True, null=True)
