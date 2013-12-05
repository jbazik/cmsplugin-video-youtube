from django.conf import settings

VALIDATE_STR = getattr(settings, 'CMS_YOUTUBE_VALIDATE_STR',
                       'http://gdata.youtube.com/feeds/api/videos/%s')

# Iframe settings
WIDTH = getattr(settings, 'CMS_YOUTUBE_DEFAULT_WIDTH', 640)
HEIGHT = getattr(settings, 'CMS_YOUTUBE_DEFAULT_HEIGHT', 360)
FULLSCREEN = getattr(settings, 'CMS_YOUTUBE_DEFAULT_FULLSCREEN', True)

# YouTube HTML5 parameters
#    If set to None, the youtube default is used
#
AUTOHIDE = getattr(settings, 'CMS_YOUTUBE_DEFAULT_AUTOHIDE', None)
AUTOPLAY = getattr(settings, 'CMS_YOUTUBE_DEFAULT_AUTOPLAY', None)
COLOR = getattr(settings, 'CMS_YOUTUBE_DEFAULT_COLOR', None)
CONTROLS = getattr(settings, 'CMS_YOUTUBE_DEFAULT_CONTROLS', None)
IV_LOAD = getattr(settings, 'CMS_YOUTUBE_DEFAULT_IV_LOAD', None)
LOOP = getattr(settings, 'CMS_YOUTUBE_DEFAULT_LOOP', None)
MODESTBRANDING = getattr(settings, 'CMS_YOUTUBE_DEFAULT_MODESTBRANDING', None)
RELATED = getattr(settings, 'CMS_YOUTUBE_DEFAULT_RELATED', None)
SHOWINFO = getattr(settings, 'CMS_YOUTUBE_DEFAULT_SHOWINFO', None)
THEME = getattr(settings, 'CMS_YOUTUBE_DEFAULT_THEME', None)

#
#    If an origin is not set, it is determined from the request if
#    django.contrib.sites is used.
#
ORIGIN = getattr(settings, 'CMS_YOUTUBE_DEFAULT_ORIGIN', None)
