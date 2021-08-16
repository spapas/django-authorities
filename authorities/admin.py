from django.contrib import admin
from .models import Authority, AuthorityKind


class AuthorityKindAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    search_fields = ("name",)


class AuthorityAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "parent",
    )
    search_fields = ("name",)
    filter_horizontal = ("users",)


admin.site.register(AuthorityKind, AuthorityKindAdmin)
admin.site.register(Authority, AuthorityAdmin)
