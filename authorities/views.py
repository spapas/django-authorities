from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Authority


class AuthorityListView(ListView):
    model = Authority
    context_object_name = 'authorities'


class AuthorityCreateView(CreateView):
    model = Authority
    fields = ('kind', 'is_active', 'parent', )


class AuthorityUpdateView(UpdateView):
    model = Authority
    context_object_name = 'authority'
    fields = ('kind', 'is_active', 'parent', )
    
    
class AuthorityDetailView(DetailView):
    model = Authority
    context_object_name = 'authority'    