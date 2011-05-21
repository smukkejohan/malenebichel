# coding=utf-8

from django.db import models
from treebeard.mp_tree import MP_Node
from django.utils.translation import ugettext_lazy as _


class Page(MP_Node):
    title = models.CharField('titel',
        max_length=255
    )
    slug = models.SlugField(_('slug'),
        max_length=50,
        help_text='Bruges til sidens URL.',
        unique=True
    )
    body = models.TextField('brødtekst',
        help_text='Sidens indhold.'
    )

    node_order_by = ['title']

    class Meta:
        verbose_name = 'side'
        verbose_name_plural = 'sider'
        

    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('page_detail', (),
            {'slug': str(self.slug)})

