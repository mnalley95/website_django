from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class AboutView(TemplateView):
    template_name = "about/about.html"
