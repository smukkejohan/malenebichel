# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Course.custom_time'
        db.add_column('courses_course', 'custom_time', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Course.location'
        db.add_column('courses_course', 'location', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Course.price'
        db.add_column('courses_course', 'price', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Course.custom_time'
        db.delete_column('courses_course', 'custom_time')

        # Deleting field 'Course.location'
        db.delete_column('courses_course', 'location')

        # Deleting field 'Course.price'
        db.delete_column('courses_course', 'price')


    models = {
        'courses.course': {
            'Meta': {'ordering': "['-start_date']", 'object_name': 'Course'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'custom_time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'price': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '55', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['courses']
