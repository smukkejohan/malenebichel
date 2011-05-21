# coding=utf-8

from datetime import datetime
from django.db import models

class FutureCourseManager(models.Manager):
    def get_query_set(self):
        return super(FutureCourseManager, self).get_query_set().filter(end_date__gte=datetime.now())

class Course(models.Model):
    title = models.CharField(
        'navn',
        max_length=255
    )
    slug = models.SlugField(max_length=55,
        help_text="Bruges til kursets egen side."
    )
    start_date = models.DateTimeField('start',
        help_text="""Hvornår starter kurset?
            Hvis kurset er spredt over flere datoer indtastes den første.
        """
    )
    end_date = models.DateTimeField('slut',
        help_text="""Hvornår slutter kurset?
            Hvis kurset er spredt over flere datoer indtastes den sidste.
            Kurser bliver vist på forsiden indtil deres slut dato.
            """
    )
    custom_time = models.CharField('brugerdefineret tid',
        max_length=255,
        help_text="""fx. 'hver torsdag aften i januar'
            eller 'd. 1/5, 6/5 og 8/5 kl. 20:15'
            Hvis feltet ikke udfyldes bruges værdierne i start og slut.
        """,
        blank=True,
    )
    location = models.CharField('sted',
        max_length=255,
        help_text="""Hvorhenne foregår kurset?
            fx. 'Sydney operaen' eller 'Ryesgade 119b'
        """,
        blank=True
    )
    price = models.PositiveIntegerField('pris',
        help_text='Hvad koster det i danske kroner at være med på kurset?',
        default=0,
    )
    description = models.TextField(
        'beskrivelse',
        help_text='En kort beskrivelse af kurset.'
    )
    body = models.TextField(
        'brødtekst',
        help_text="En længere detaljeret beskrivelse af kurset der bliver vist på sin egen side.",
        blank=True
    )
    
    objects = models.Manager()
    future_objects = FutureCourseManager()

    def __unicode__(self):
        return u'%s' % self.title
    
    class Meta:
        verbose_name = 'kursus'
        verbose_name_plural = 'kurser'
        get_latest_by = "start_date"
        ordering = ['-start_date']