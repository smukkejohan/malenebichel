# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Praise.excerpt'
        db.add_column('praise_praise', 'excerpt', self.gf('django.db.models.fields.CharField')(default='a', max_length=255), keep_default=False)

        # Adding field 'Praise.cite'
        db.add_column('praise_praise', 'cite', self.gf('django.db.models.fields.CharField')(default='a', max_length=255), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Praise.excerpt'
        db.delete_column('praise_praise', 'excerpt')

        # Deleting field 'Praise.cite'
        db.delete_column('praise_praise', 'cite')


    models = {
        'praise.praise': {
            'Meta': {'object_name': 'Praise'},
            'cite': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'excerpt': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['praise']
