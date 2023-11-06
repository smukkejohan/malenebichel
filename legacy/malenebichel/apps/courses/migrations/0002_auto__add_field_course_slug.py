# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Course.slug'
        db.add_column('courses_course', 'slug', self.gf('django.db.models.fields.SlugField')(default='a', max_length=55, db_index=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Course.slug'
        db.delete_column('courses_course', 'slug')


    models = {
        'courses.course': {
            'Meta': {'ordering': "['-start_date']", 'object_name': 'Course'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '55', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['courses']
