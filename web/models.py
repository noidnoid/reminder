from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Expense(models.Model):

    text = models.CharField(max_length = 255, default='')
    dong = models.CharField(max_length = 255, default='',null=True, blank=True)
    amount = models.BigIntegerField(default = '')
    user = models.ForeignKey(User, default = '')
    date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return (self.text)

class Income(models.Model):

    text = models.CharField(max_length = 255, default='')
    dong = models.CharField(max_length = 255, default='',null=True, blank=True)
    amount = models.BigIntegerField(default = '')
    user = models.ForeignKey(User, default = '')
    date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return '{}{}'.format(self.text, self.date)


class Token(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE)
    token = models.CharField(max_length = 200)

    def __unicode__(self):
        return "{}_token".format(self.user )
