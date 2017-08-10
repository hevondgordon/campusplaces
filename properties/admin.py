# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin

from properties.models import Room, Picture, Property, Address

# list display definition


class RoomAdmin(admin.ModelAdmin):
    list_display = ('price', 'accomodation', 'own_kitchen', 'own_bathroom')


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('landlord', 'lat', 'lng', 'telephone_number')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_line_1', 'address_line_2')

# Register your models here.


admin.site.register(Room, RoomAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Picture)
admin.site.register(Address, AddressAdmin)
