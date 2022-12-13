from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatars', null=True, blank = True)