from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import importlib


def default_name_str(self):
    return "{0}: {1}".format(self.id, self.name)


def get_function(function_name):
    parts = function_name.split(".")
    name = parts[-1]
    module_path = ".".join(parts[:-1])
    module = importlib.import_module(module_path)
    return getattr(module, name)


try:
    authority_str_function = get_function(settings.AUTHORITY_STR_FUNCTION)
except:
    authority_str_function = default_name_str

try:
    authority_kind_str_function = get_function(settings.AUTHORITY_KIND_STR_FUNCTION)
except:
    authority_kind_str_function = default_name_str


class NamedModel(models.Model):
    
    code = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        help_text=_(
            "Optional field to add an organization-specific code in addition to the name"
        ),
    )

    class Meta:
        abstract = True


class AuthorityKind(NamedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"), unique=True)
    class Meta:
        verbose_name = _("Authority Kind")
        verbose_name_plural = _("Authority Kinds")

    def __str__(self):
        return authority_kind_str_function(self)


class Authority(NamedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    kind = models.ForeignKey(
        "AuthorityKind",
        verbose_name=_(
            "Kind",
        ),
        on_delete=models.PROTECT,
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_("Unselect this if the authority is not active any more"),
    )
    parent = models.ForeignKey(
        "self",
        verbose_name=_(
            "Parent",
        ),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name=_(
            "Email",
        ),
        blank=True,
        null=True,
    )
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Authority users"),
        related_name="authorities",
        blank=True,
    )

    def get_absolute_url(self):
        return reverse("authority_view", args=[str(self.id)])

    class Meta:
        verbose_name = _("Authority")
        verbose_name_plural = _("Authorities")
        unique_together = ("name", "kind")

    def __str__(self):
        return authority_str_function(self)
