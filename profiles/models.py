from django.db import models

# Create your models here.
class Profile(models.Model):
    """
    docstring
    """
    content = models.TextField()
    