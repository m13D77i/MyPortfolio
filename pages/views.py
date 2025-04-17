from django.shortcuts import render
from django.views.generic import *

from .forms import MessageForm

class HomePageView(TemplateView):
    template_name = "pages/home.html"


def contact_page_view(request):

    return render(
        request, "pages/contact.html",
    )
