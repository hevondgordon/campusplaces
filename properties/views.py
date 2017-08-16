# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from models import Room, Picture, Property


# Create your views here.
class HomePageView(ListView):
    template_name = 'index.html'
    model = Room
    context_object_name = 'rooms'
    paginate_by = 20

    # def get_queryset(self):
    #     location = self.request.GET.get('location')
    #     accomodation = self.request.GET.get('accomodation')
    #     range = self.request.GET.get('range')

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        accomodations = request.GET.get('accomodations')
        range_from = 0
        range_to = 100000
        range = request.GET.get('range')
        if range:
            ranges = range.split(';')
            range_from = ranges[0]
            range_to = ranges[1]

        context.update({"from": range_from, "to": range_to})
        if accomodations is None or accomodations == "":
            accomodation = {"accomodation": "single"}
        else:
            accomodation = {"accomodation": accomodations}

        context.update(accomodation)
        return self.render_to_response(context)


class ProfileView():
    pass
