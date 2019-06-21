from django.db import models
from django.urls import reverse
# Create your models here.

class Wish(models.Model):
    description = models.CharField(max_length = 100)

    def get_absolute_url(self):
        return reverse('wishes_index')