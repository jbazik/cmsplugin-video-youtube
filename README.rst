=======================
cmsplugin-video-youtube
=======================
Yet another YouTube video plugin for django-cms.  Inspired by the
various others.

Features
========
* Uses the iframe embed method
* Allows setting most AS3/HTML5 parameters
* Text plugin enabled
* Provides thumbnail image for edit icon
* Validates video id against youtube.com
* Uses south for data migrations

Requirements
============
* Django
* django-cms

Settings
========
* CMS_YOUTUBE_VALIDATE_STR

  A python format string with one (video_id) argument that is a url to
  use to validate the user-provided video_id.  Successful validation
  should return HTTP code 200.  Set this to None to disable validation.

The following settings establish defaults for new videos.  Each of these
values can be set per-video.

* CMS_YOUTUBE_DEFAULT_WIDTH

  Player width, in pixels.  Default is 640.

* CMS_YOUTUBE_DEFAULT_HEIGHT

  Player height, in pixels.  Default is 360 (360p).

* CMS_YOUTUBE_DEFAULT_FULLSCREEN

  Provide "full screen" button.  Default is True.

YouTube Parameter Defaults
--------------------------
The following settings are optional, and if not set the player default
is used.  Each of these can also be set per-video.  For descriptions
and defaults, see:
`<https://developers.google.com/youtube/player_parameters#Parameters>`_

* CMS_YOUTUBE_DEFAULT_AUTOHIDE

* CMS_YOUTUBE_DEFAULT_AUTOPLAY

* CMS_YOUTUBE_DEFAULT_COLOR

* CMS_YOUTUBE_DEFAULT_CONTROLS

* CMS_YOUTUBE_DEFAULT_IV_LOAD

* CMS_YOUTUBE_DEFAULT_LOOP

* CMS_YOUTUBE_DEFAULT_MODESTBRANDING

* CMS_YOUTUBE_DEFAULT_ORIGIN

  If not set and django.contrib.sites is installed, the domain of the
  current site is used.

* CMS_YOUTUBE_DEFAULT_RELATED

* CMS_YOUTUBE_DEFAULT_SHOWINFO

* CMS_YOUTUBE_DEFAULT_THEME
