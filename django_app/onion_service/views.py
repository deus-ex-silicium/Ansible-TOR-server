from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class IndexView(View):
    """ Main View for django service """

    def get(self, request, *args, **kwargs):
        return HttpResponse("This is django onion service")
