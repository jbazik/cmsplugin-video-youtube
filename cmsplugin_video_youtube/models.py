from django.db import models
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin

from cmsplugin_video_youtube import settings


class YouTubeVideo(CMSPlugin):
    AUTOHIDE_CHOICES = (
        (0, _("0 - Don't hide controls")),
        (1, _("1 - Hide controls after start")),
        (2, _("2 - Hide progress bar only after start")),
    )
    COLOR_CHOICES = (
        ('red', _('Red')),
        ('white', _('White')),
    )
    CONTROL_CHOICES = (
        (0, _("0 - Hide video controls, load flash player")),
        (1, _("1 - Show video controls, load flash player")),
        (2, _("2 - Show video controls, delay loading flash player")),
    )
    IV_LOAD_CHOICES = (
        (1, _("1 - Show annotations")),
        (3, _("3 - Hide annotations")),
    )
    THEME_CHOICES = (
        ('dark', _('Dark')),
        ('light', _('Light')),
    )
    NULL_BOOLEAN_CHOICES = (
        (None, '---------'),
        (True, 'Yes'),
        (False, 'No'),
    )

    name = models.CharField(_('name'), max_length=255)
    video_id = models.CharField(_('video id'), max_length=60)

    # iframe parameters
    width = models.IntegerField(_('width'), default=settings.WIDTH)
    height = models.IntegerField(_('height'), default=settings.HEIGHT)
    fullscreen = models.BooleanField(_('allow fullscreen'),
                                     default=settings.FULLSCREEN)

    # YouTube HTML5 parameters - all optional
    autohide = models.PositiveSmallIntegerField(_('autohide'),
                                                null=True, blank=True,
                                                choices=AUTOHIDE_CHOICES,
                                                default=settings.AUTOHIDE)
    autoplay = models.NullBooleanField(_('autoplay'), null=True, blank=True,
                                       choices=NULL_BOOLEAN_CHOICES,
                                       default=settings.AUTOPLAY)
    color = models.CharField(_('color'), max_length=10, blank=True,
                             choices=COLOR_CHOICES, default=settings.COLOR)
    controls = models.PositiveSmallIntegerField(_('controls'),
                                                null=True, blank=True,
                                                choices=CONTROL_CHOICES,
                                                default=settings.CONTROLS)
    iv_load = models.PositiveSmallIntegerField(_('iv load policy'),
                                               null=True, blank=True,
                                               choices=IV_LOAD_CHOICES,
                                               default=settings.IV_LOAD)
    loop = models.NullBooleanField(_('loop'), null=True, blank=True,
                                   choices=NULL_BOOLEAN_CHOICES,
                                   default=settings.LOOP)
    modestbranding = models.NullBooleanField(_('modest branding'),
                                             null=True, blank=True,
                                             choices=NULL_BOOLEAN_CHOICES,
                                             default=settings.MODESTBRANDING)
    playlist = models.TextField(_('playlist'), blank=True,
               help_text=_('Space- or line-separated list of video ids.'))
    related = models.NullBooleanField(_('display related videos'),
                                      null=True, blank=True,
                                      choices=NULL_BOOLEAN_CHOICES,
                                      default=settings.RELATED)
    showinfo = models.NullBooleanField(_('show video information'),
                                       null=True, blank=True,
                                       choices=NULL_BOOLEAN_CHOICES,
                                       default=settings.SHOWINFO)
    start = models.PositiveIntegerField(_('start'), null=True, blank=True)
    theme = models.CharField(_('theme'), max_length=10, blank=True,
                             choices=THEME_CHOICES, default=settings.THEME)

    search_fields = ('name', 'video_id')

    def __unicode__(self):
        return u'%s:%s' % (self.name, self.video_id)
