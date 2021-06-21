from django.db import models


class Role(models.Model):
    """
    Role Details
    """
    name = models.CharField(max_length=70)
    description = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

