from django.db import models


class Zavod(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)

    def __str__(self):
        return self.name


class Vloyat(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)

    def __str__(self):
        return self.name


class Mashena(models.Model):
    name = models.CharField(max_length=125, blank=False, null=False)
    color = models.CharField(max_length=250, blank=False, null=False)
    type = models.IntegerField(blank=False, null=False, default=0)
    vloyat = models.ForeignKey(Vloyat, blank=False, null=True, on_delete=models.SET_NULL)
    zavod = models.ForeignKey(Zavod, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
