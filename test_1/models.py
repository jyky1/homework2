from django.db import models

# Create your models here.
class Post1(models.Model):
    title = models.CharField(max_length=15)
    def __str__(self) -> str:
        return self.title
