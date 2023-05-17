from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=35)
    description = models.TextField()
    PRIORITY_OPTIONS = (
        (1, "High"),
        (2, "Normal"),
        (3, "Low")
    )
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_OPTIONS, default=2)
    done = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task