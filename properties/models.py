# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_extensions.db.models import TimeStampedModel
from django.db import models

from authentication.models import User

import constants
# Create your models here.


class Picture(TimeStampedModel):
    image = models.ImageField(blank=True)

    def __str__(self):
        return "Picture Number {}".format(self.pk)


class Room(TimeStampedModel):
    images = models.ManyToManyField(Picture, blank=True)
    price = models.PositiveIntegerField()
    accomodation = models.CharField(
        max_length=20,
        choices=constants.ACCOMODATIONS,
        default=constants.SINGLE,
    )
    likes = models.ManyToManyField(
        User,
        verbose_name="likes",
        blank=True,
    )
    own_kitchen = models.BooleanField(
        default=False,
        verbose_name="has own kitchen"
    )
    own_bathroom = models.BooleanField(
        default=False,
        verbose_name="has own bathroom"
    )

    def __str__(self):
        return "Room Number {}".format(self.pk)


class Address(TimeStampedModel):
    parish = models.CharField(
        max_length=50,
        choices=constants.PARISHES,
        default=constants.DEFAULT_PARISH,
    )
    address_line_1 = models.CharField(
        max_length=255,
        default='',
        blank=True
    )
    address_line_2 = models.CharField(
        max_length=255,
        default='',
        blank=True
    )

    class Meta:
        verbose_name = "Address"

    def __str__(self):
        return "Address Number {}".format(self.pk)


class Telephone(TimeStampedModel):
    cell_phone = models.CharField(
        max_length=255,
        default='',
        blank=True
    )
    home_phone = models.CharField(
        max_length=255,
        default='',
        blank=True
    )
    work_phone = models.CharField(
        max_length=255,
        default='',
        blank=True
    )
    ext = models.CharField(
        max_length=255,
        default='',
        blank=True
    )

    class Meta:
        verbose_name = "Telephone"

    def __str__(self):
        return "Telephone Number {}".format(self.pk)


class Property(TimeStampedModel):
    landlord = models.ForeignKey(User, related_name="property")
    rooms = models.ManyToManyField(Room, related_name="property", blank=True)
    images = models.ManyToManyField(Picture, blank=True)
    lat = models.PositiveIntegerField(null=True, blank=True)
    lng = models.PositiveIntegerField(null=True, blank=True)
    telephone_number = models.ForeignKey(
        Telephone, verbose_name="Telephone", related_name="telephone",
        null=True, blank=True
    )
    address = models.ForeignKey(
        Address, verbose_name="Address", related_name="address", null=True, blank=True
    )

    class Meta:
        verbose_name = "Property"

    def __str__(self):
        return "Property Number {}".format(self.pk)
