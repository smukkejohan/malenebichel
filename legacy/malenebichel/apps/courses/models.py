# coding=utf-8

from datetime import datetime
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

class PublicManager(models.Manager):
    def get_query_set(self):
        qs = super(PublicManager, self).get_query_set()
        qs = qs.filter(status=Course.PUBLIC_STATUS)
        return qs

class FutureManager(PublicManager):
    def get_query_set(self):
        return super(FutureManager, self).get_query_set().filter(end_date__gte=datetime.now())

class SignupManager(FutureManager):
    def get_query_set(self):
        return super(SignupManager, self).get_query_set().filter(signup_open=True)

class Course(models.Model):
    """
    A Course has a start and end date and information about the course

    """


    DRAFT_STATUS = 0
    PUBLIC_STATUS = 1
    ARCHIVE_STATUS = 2
    STATUS_CHOICES = (
        (DRAFT_STATUS, 'Kladde'),
        (PUBLIC_STATUS, 'Offentlig'),
        (ARCHIVE_STATUS, 'Arkiveret'),
    )

    display_frontpage = models.BooleanField(
        'Vis på forsiden',
        default=True)

    title = models.CharField(
        'navn',
        max_length=255
    )
    slug = models.SlugField(max_length=55,
        help_text="Bruges til kursets egen side.",
        unique=True
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

    signup_open = models.BooleanField(
        'Tilmelding åben',
        default=False,
        help_text="Er kurset åbent for tilmeldinger?")

    signup_link = models.URLField(
        'Tilmeldings link',
        help_text="Link til tilmelding på fx. Docas.",
        blank=True)

    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS)

    post_date = models.DateTimeField(default=datetime.now, editable=False)

    objects = models.Manager()
    public_objects = PublicManager()
    future_objects = FutureManager()
    signup_objects = SignupManager()

    def __unicode__(self):
        return self.title


    @models.permalink
    def get_absolute_url(self):
        return ('course_detail', (),
            {'slug': str(self.slug)})

    def get_sign_up_url(self):
        return u"%s?course=%d" % (reverse('course_signup'), self.pk)

    class Meta:
        verbose_name = 'kursus'
        verbose_name_plural = 'kurser'
        get_latest_by = "start_date"
        ordering = ['-start_date']

class Signup(models.Model):
    """
    Users can sign up to courses providing raw information or a foreignkey to a user model

    """

    course = models.ForeignKey(Course)
    user = models.ForeignKey(User, null=True, blank=True)

    email = models.EmailField(max_length=150)
    phone = models.CharField('Telefon', blank=True, max_length=16)
    first_name = models.CharField('Fornavn', max_length=150)
    last_name = models.CharField('Efternavn', max_length=150)
    time = models.DateTimeField('Tid', default=datetime.now, editable=False)
    note = models.TextField('Note', blank=True)

    def __unicode__(self):
        return u"%s tilmeldt til %s" % (self.first_name, self.course.title)
