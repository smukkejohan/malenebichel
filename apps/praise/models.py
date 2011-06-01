# coding=utf-8

from django.core.urlresolvers import reverse
from django.db import models
from sorl.thumbnail import ImageField

class Praise(models.Model):
    excerpt = models.CharField('Kort uddrag', max_length=255, help_text="Vises på forsiden.")
    content = models.TextField('Anbefaling', help_text="Anbefalingen i fuld længde, vises efter man klikker på uddraget på forsiden.")
    person = models.CharField('Henvisning', max_length=255, help_text="Hvem har givet anbefalingen. Fx. Jette Andersen, Kims Chips")
    image = ImageField(
        upload_to='images/praise/',
        blank=True,
        null=True,
        help_text='Billede af personen som har givet anbefalingen.'
    )

    def __unicode__(self):
        return u'"%s" - %s' % (self.excerpt, self.person)

    def get_absolute_url(self):
        return '%s#p%s' % (reverse('praises'), str(self.pk))
