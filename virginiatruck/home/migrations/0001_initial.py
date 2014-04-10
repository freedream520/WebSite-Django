# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'home_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('company_phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('company_fax', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('company_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('company_address', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('company_msg', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'home', ['Company'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'home_company')


    models = {
        u'home.company': {
            'Meta': {'object_name': 'Company'},
            'company_address': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'company_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'company_fax': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'company_msg': ('django.db.models.fields.TextField', [], {}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'company_phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['home']