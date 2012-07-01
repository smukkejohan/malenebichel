# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Praise'
        db.create_table('praise_praise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('praise', ['Praise'])


    def backwards(self, orm):
        
        # Deleting model 'Praise'
        db.delete_table('praise_praise')


    models = {
        'praise.praise': {
            'Meta': {'object_name': 'Praise'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['praise']
