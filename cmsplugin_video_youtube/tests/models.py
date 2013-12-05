from django.test import TestCase

from cmsplugin_video_youtube.models import YouTubeVideo

class ModelTests(TestCase):

    def test_instantiation(self):
        video = YouTubeVideo()
        self.assertTrue(video)
