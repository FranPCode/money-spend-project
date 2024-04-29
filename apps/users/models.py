from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):

        if not self.pk or self._password != self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
