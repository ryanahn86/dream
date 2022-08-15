from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
#from django.urls import reverse

class IndexView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class WhatView(TemplateView):
    template_name = 'what.html'

class WhyView(TemplateView):
    template_name = 'why.html'

class HowView(TemplateView):
    template_name = 'how.html'

class ReviewView(TemplateView):
    template_name = 'review.html'
