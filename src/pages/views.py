from django.views.generic import TemplateView, ListView

from shelters.models import Shelter


class HomePageView(ListView):
    model = Shelter
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
