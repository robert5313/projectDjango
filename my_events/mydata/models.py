from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    starts_at=models.DateTimeField(default=timezone.now)
    ends_at=models.DateField(validators=[MinValueValidator(limit_value=timezone.now().date())])
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (
            f"{self.name}"
            f"{self.description }"
            f"({self.starts_at: %Y-%m-%d %H:%M}):"
        )