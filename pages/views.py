from django.shortcuts import render
from django.views.generic import *

class HomePageView(TemplateView):
    template_name = "pages/home.html"

