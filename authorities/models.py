from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class NamedModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'), unique=True )
    code = models.CharField(max_length=32, blank=True, null=True, help_text=_('Optional field to add an organization-specific code in addition to the name'))

    def __str__(self):
        return '{0}: {1}'.format(self.id, self.name)

    class Meta:
        abstract=True


class AuthorityKind(NamedModel):
    class Meta:
        verbose_name = _('Authority Kind')
        verbose_name_plural = _('Authority Kinds')


class Authority(NamedModel):
    kind = models.ForeignKey('AuthorityKind' , verbose_name= _('Kind',), on_delete=models.PROTECT )
    is_active = models.BooleanField(default=True, help_text=_('Unselect this if the authority is not active any more'))
    parent = models.ForeignKey('self' , verbose_name= _('Parent',), on_delete=models.PROTECT, blank=True, null=True, )
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_('Authority users'), related_name='authorities', blank=True)

    def get_absolute_url(self):
        return reverse('authority_view', args=[str(self.id)])

    class Meta:
        verbose_name = _('Authority')
        verbose_name_plural = _('Authorities')
