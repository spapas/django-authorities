from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class NamedModel(models.Model):
    name = models.CharField(max_length=255, verbose_name = 'Όνομα', unique=True )

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
    parent = models.ForeignKey('self' , verbose_name= _('Parent',), on_delete=models.PROTECT, blank=True, null=True, )
    # The M2M is not really needed - I'm adding it to use it instead of adding a user *Profile* object.
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_('Authority users'), related_name='authorities', blank=True)

    
    class Meta:
        verbose_name = _('Authority')
        verbose_name_plural = _('Authorities')
