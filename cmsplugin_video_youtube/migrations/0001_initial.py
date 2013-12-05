# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'YouTubeVideo'
        db.create_table('cmsplugin_youtubevideo', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('video_id', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=640)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=360)),
            ('fullscreen', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('autohide', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('autoplay', self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(default=None, max_length=10, null=True, blank=True)),
            ('controls', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('iv_load', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('loop', self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True)),
            ('modestbranding', self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True)),
            ('playlist', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('related', self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True)),
            ('showinfo', self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True)),
            ('start', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('theme', self.gf('django.db.models.fields.CharField')(default=None, max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal('cmsplugin_video_youtube', ['YouTubeVideo'])


    def backwards(self, orm):
        # Deleting model 'YouTubeVideo'
        db.delete_table('cmsplugin_youtubevideo')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 12, 5, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_video_youtube.youtubevideo': {
            'Meta': {'object_name': 'YouTubeVideo', 'db_table': "'cmsplugin_youtubevideo'", '_ormbases': ['cms.CMSPlugin']},
            'autohide': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'autoplay': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'controls': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'fullscreen': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '360'}),
            'iv_load': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'loop': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'modestbranding': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'playlist': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'related': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'showinfo': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'theme': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '640'})
        }
    }

    complete_apps = ['cmsplugin_video_youtube']