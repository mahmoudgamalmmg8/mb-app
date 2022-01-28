from importlib.resources import contents
from re import template
from django.shortcuts import render
from django.views.generic import ListView
from .models import post
# Create your views here.
class HomePageView(ListView):
    model = post
    template_name = 'home.html'
    context_object_name = 'all_posts_lists'