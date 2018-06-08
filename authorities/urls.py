from django.contrib import admin
from django.urls import path
from .views import AuthorityListView, AuthorityCreateView, AuthorityUpdateView, AuthorityDetailView, AuthorityEditUsersView


urlpatterns = [

    path('', AuthorityListView.as_view(), name='authority_list', ),
    path('create', AuthorityCreateView.as_view(), name='authority_create', ),
    path('update/<int:pk>/', AuthorityUpdateView.as_view(), name='authority_update', ),
    path('view/<int:pk>/', AuthorityDetailView.as_view(), name='authority_view', ),
    path('update_users/<int:pk>/', AuthorityEditUsersView.as_view(), name='authority_update_users', ),
]
