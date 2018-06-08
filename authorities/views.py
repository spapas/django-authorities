from django.shortcuts import render
from django.views.generic import ListView
from .models import Authority

class AuthorityListView(ListView):
    model = Authority
    context_object_name = 'authorities'