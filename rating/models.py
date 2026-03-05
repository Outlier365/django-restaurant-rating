from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

# Create your models here.
class Restaurant(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="restaurants",
        null=True,      # 先允許 null（為了處理你現有資料）
        blank=True
    )

    name = models.CharField(max_length=30)
    score = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0)
        ]
    )
    review = models.TextField(max_length=500)
    def __str__(self):
        return self.name