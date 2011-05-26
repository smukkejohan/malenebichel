# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Praise.cite'
        db.delete_column('praise_praise', 'cite')

        # Adding field 'Praise.person'
        db.add_column('praise_praise', 'person', self.gf('django.db.models.fields.CharField')(default='a', max_length=255), keep_default=False)


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Praise.cite'
        raise RuntimeError("Cannot reverse this migration. 'Praise.cite' and its values cannot be restored.")

        # Deleting field 'Praise.person'
        db.delete_column('praise_praise', 'person')


    models = {
        'praise.praise': {
            'Meta': {'object_name': 'Praise'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'excerpt': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['praise']
