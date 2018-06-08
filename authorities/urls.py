from django.contrib import admin
from django.urls import path
from .views import AuthorityListView

urlpatterns = [

    path('', AuthorityListView.as_view(), name='authority_list', ),
]
