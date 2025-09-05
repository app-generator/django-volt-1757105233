# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Rdc(models.Model):

    #__Rdc_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)

    #__Rdc_FIELDS__END

    class Meta:
        verbose_name        = _("Rdc")
        verbose_name_plural = _("Rdc")


class Flow(models.Model):

    #__Flow_FIELDS__
    rdc = models.ForeignKey(rdc, on_delete=models.CASCADE)

    #__Flow_FIELDS__END

    class Meta:
        verbose_name        = _("Flow")
        verbose_name_plural = _("Flow")


class Sigconfi(models.Model):

    #__Sigconfi_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Sigconfi_FIELDS__END

    class Meta:
        verbose_name        = _("Sigconfi")
        verbose_name_plural = _("Sigconfi")


class Processo(models.Model):

    #__Processo_FIELDS__
    flow = models.ForeignKey(flow, on_delete=models.CASCADE)
    sig = models.ForeignKey(sigconfi, on_delete=models.CASCADE)
    status = models.IntegerField(null=True, blank=True)

    #__Processo_FIELDS__END

    class Meta:
        verbose_name        = _("Processo")
        verbose_name_plural = _("Processo")



#__MODELS__END
