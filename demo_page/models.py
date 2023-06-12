from django.db import models


class Logg(models.Model):
    ip_addr = models.CharField(max_length=16)
    visits = models.IntegerField(default=0)
    last_visit = models.DateTimeField(auto_now=True)
