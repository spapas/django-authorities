from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Authority
from .forms import AuthorityUsersModelForm


class AuthorityListView(ListView):
    model = Authority
    context_object_name = "authorities"


class AuthorityCreateView(CreateView):
    model = Authority
    fields = (
        "name",
        "kind",
        "is_active",
        "parent",
        "email",
    )


class AuthorityUpdateView(UpdateView):
    model = Authority
    context_object_name = "authority"
    fields = (
        "name",
        "kind",
        "is_active",
        "parent",
        "email",
    )


class AuthorityDetailView(DetailView):
    model = Authority
    context_object_name = "authority"


class AuthorityEditUsersView(
    UpdateView,
):
    model = Authority
    form_class = AuthorityUsersModelForm
    # template_name='authorities/authority_edit_users.html'
    context_object_name = "authority"

    def get_form_kwargs(self):
        kwargs = super(AuthorityEditUsersView, self).get_form_kwargs()
        return kwargs
