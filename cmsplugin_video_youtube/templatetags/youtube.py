from django import template

from cmsplugin_video_youtube.settings import ORIGIN

try:
    from django.contrib.sites.models import get_current_site
except ImportError:
    pass

register = template.Library()

ytparams = (
    #property, ytname
    #--------  ------
    ('autohide', 'autohide'),
    ('autoplay', 'autoplay'),
    ('color', 'color'),
    ('controls', 'controls'),
    ('iv_load', 'iv_load_policy'),
    ('loop', 'loop'),
    ('modestbranding', 'modestbranding'),
    ('playlist', 'playlist'),
    ('related', 'rel'),
    ('showinfo', 'showinfo'),
    ('start', 'start'),
    ('theme', 'theme'),
)

@register.simple_tag(takes_context=True)
def youtube_params(context, object):
    """
    Returns a parameter string based on video object settings suitable
    for appending to a youtube url.  Returns only non-null values.
    """
    params = {}
    for prop, param in ytparams:
        val = getattr(object, prop, None)
        if val is not None:
            if val is True:
                params[param] = 1
            elif val is False:
                params[param] = 0
            elif param == 'playlist':
                if val.strip():
                    params[param] = ','.join(
                              [a for b in val.splitlines() for a in b.split()])
            else:
                params[param] = val
    if ORIGIN:
        params['origin'] = ORIGIN
    elif 'request' in context:
        request = context['request']
        try:
            site = get_current_site(request)
            if hasattr(request, 'scheme'):
                scheme = request.scheme
            else:
                scheme = 'http'
            params['origin'] = "%s://%s" % (scheme, site.domain)
        except NameError:
            pass

    if params:
        return '?' + '&'.join(['%s=%s' % (k,v) for k,v in params.items()])
    else:
        return ''
