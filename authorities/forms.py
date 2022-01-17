from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import Authority


class AuthorityUsersModelForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=get_user_model().objects.all(),
        label=_("Select users"),
        required=False,
    )

    class Meta:
        model = Authority
        fields = ("users",)

    def __init__(self, *args, **kwargs):
        super(AuthorityUsersModelForm, self).__init__(*args, **kwargs)
