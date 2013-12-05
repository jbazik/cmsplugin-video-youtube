#!/usr/bin/python

import os, sys
from django.conf import settings

ROOT = os.path.abspath(os.path.join(
                       os.path.dirname(__file__), os.pardir, os.pardir))

sys.path.append(ROOT)
settings.configure(DEBUG = True,
                   DATABASES = {
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                           'NAME': 'test.sqlite3',
                       }
                   },
                   ROOT_URLCONF = 'cms.urls',
                   TEMPLATE_CONTEXT_PROCESSORS = (
                       'django.core.context_processors.request',
                   ),
                   INSTALLED_APPS = ('django.contrib.auth',
                                     'django.contrib.contenttypes',
                                     'django.contrib.sites',
                                     'cms',
                                     'mptt',
                                     'cmsplugin_video_youtube',),
)

from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(['cmsplugin_video_youtube',])
if failures:
    sys.exit(failures)
