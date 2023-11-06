# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Praise.image'
        db.add_column('praise_praise', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Praise.image'
        db.delete_column('praise_praise', 'image')


    models = {
        'praise.praise': {
            'Meta': {'object_name': 'Praise'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'excerpt': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['praise']
