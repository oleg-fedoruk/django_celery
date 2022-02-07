from django.db import models


class TwoIntegers(models.Model):
    first = models.IntegerField(verbose_name='first')
    second = models.IntegerField(verbose_name='second')
