from setuptools import find_packages, setup

setup(name='cmsplugin-video-youtube',
    version='0.1',
    description='Embedded YouTube video plugin for django-cms',
    author='John Bazik',
    author_email='jsb@cs.brown.edu',
    url='https://github.com/jbazik/cmsplugin-video-youtube/',
    packages=find_packages(),
    include_package_data = True,
    provides=['cmsplugin_video_youtube'],
    license='LGPL',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    ],
)
