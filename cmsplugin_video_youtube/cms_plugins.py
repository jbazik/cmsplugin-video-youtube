from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_video_youtube.models import YouTubeVideo
from cmsplugin_video_youtube.forms import YouTubeVideoForm


class YouTubeVideoPlugin(CMSPluginBase):
    model = YouTubeVideo
    name = _("YouTubeVideo")
    render_template = "cmsplugin_video_youtube/embed.html"
    form = YouTubeVideoForm
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': ('name', 'video_id', 'width', 'height'),
        }),
        ('Advanced Options', {
            'classes': ('collapse',),
            'fields': (
                'fullscreen',
                'autohide',
                'autoplay',
                'color',
                'controls',
                'iv_load',
                'loop',
                'modestbranding',
                'playlist',
                'related',
                'showinfo',
                'start',
                'theme',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder
        })
        return context

    def icon_src(self, instance):
        return u"http://img.youtube.com/vi/%s/default.jpg" % instance.video_id

    def icon_alt(self, instance):
        return u"%s" % instance

plugin_pool.register_plugin(YouTubeVideoPlugin)
