from httplib import HTTPConnection
from urlparse import urlsplit, urlunsplit

from django.utils.translation import ugettext as _
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from cmsplugin_video_youtube.settings import VALIDATE_STR
from cmsplugin_video_youtube.models import YouTubeVideo


class YouTubeVideoForm(ModelForm):

    def clean_video_id(self):
        """
        Validate video id by hitting against youtube.
        """
        video_id = self.cleaned_data['video_id']
        if VALIDATE_STR:
            url = urlsplit(VALIDATE_STR % video_id)
            conn = HTTPConnection(url.netloc)
            conn.request("GET", urlunsplit(('','',url.path,url.query,'')))
            resp = conn.getresponse()
            if resp.status != 200:
                raise ValidationError(_("Video not found"))
        return video_id

    class Meta:
        model = YouTubeVideo
