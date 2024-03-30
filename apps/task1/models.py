from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import uuid


class NonDeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    objects = models.Manager()
    active_objects = NonDeletedManager()

    class Meta:
        abstract = True


class User(SoftDeleteModel):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=128)

    objects = models.Manager()  # The default manager.
    active_objects = NonDeletedManager()  # Our custom manager.

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    @classmethod
    def create_user(cls, username, password, email=None):
        user = cls(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def soft_delete(self):
        self.is_deleted = True
        self.username = self.username + uuid.uuid4().hex[:6].upper()
        self.save()
        return self
