from django.core.urlresolvers import reverse
from django.db import models

class Praise(models.Model):
    excerpt = models.CharField('Kort uddrag', max_length=255)
    content = models.TextField('Anbefaling')
    person = models.CharField('Henvisning', max_length=255)

    def __unicode__(self):
        return u'"%s" - %s' % (self.excerpt, self.person)

    def get_absolute_url(self):
        return '%s#p%s' % (reverse('praises'), str(self.pk))
