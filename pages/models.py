from django.db import models
from django.utils.translation import gettext_lazy as _

class Message(models.Model):
    fullname = models.CharField(max_length=60, verbose_name=_("full name"), blank=True)
    email = models.EmailField(verbose_name=_("email address"))
    subject = models.CharField(max_length=250, verbose_name=_("subject"))
    description = models.TextField(verbose_name=_("description"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("datatime created"))


    def __str__(self):
        return self.fullname
