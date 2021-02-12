from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.utils import long_uid


class User(AbstractUser):
    pass


class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(max_length=40, default=long_uid, db_index=True, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tokens')
    created_at = models.DateTimeField(auto_now_add=True)
