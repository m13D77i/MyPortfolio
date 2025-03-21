from django.db import models


class Customer(models.Model):
    fullname = models.CharField(max_length=50, verbose_name="full name")
    email = models.EmailField(unique=True, verbose_name="email address")
    subject = models.CharField(max_length=250, verbose_name="subject")
    description = models.TextField(verbose_name="description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="datatime created")


    def __str__(self):
        return self.fullname
