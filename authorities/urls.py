from django.contrib import admin
from django.urls import path
from .views import (
    AuthorityListView,
    AuthorityCreateView,
    AuthorityUpdateView,
    AuthorityDetailView,
    AuthorityEditUsersView,
)
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path(
        "",
        permission_required("authorities.view_authority")(AuthorityListView.as_view()),
        name="authority_list",
    ),
    path(
        "create",
        permission_required("authorities.add_authority")(AuthorityCreateView.as_view()),
        name="authority_create",
    ),
    path(
        "update/<int:pk>/",
        permission_required("authorities.change_authority")(
            AuthorityUpdateView.as_view()
        ),
        name="authority_update",
    ),
    path(
        "view/<int:pk>/",
        permission_required("authorities.view_authority")(
            AuthorityDetailView.as_view()
        ),
        name="authority_view",
    ),
    path(
        "update_users/<int:pk>/",
        permission_required("authorities.change_authority")(
            AuthorityEditUsersView.as_view()
        ),
        name="authority_update_users",
    ),
]
