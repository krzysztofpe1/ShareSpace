from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    friends = models.ManyToManyField("self", related_name="user_friends")

    def add_friend(self, user) -> None:
        self.friends.add(user)

    def __str__(self):
        return self.username
