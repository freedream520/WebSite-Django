# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Company.company_phone'
        db.delete_column(u'home_company', 'company_phone')

        # Deleting field 'Company.company_fax'
        db.delete_column(u'home_company', 'company_fax')

        # Deleting field 'Company.company_name'
        db.delete_column(u'home_company', 'company_name')

        # Deleting field 'Company.company_address'
        db.delete_column(u'home_company', 'company_address')

        # Deleting field 'Company.company_msg'
        db.delete_column(u'home_company', 'company_msg')

        # Deleting field 'Company.company_email'
        db.delete_column(u'home_company', 'company_email')

        # Adding field 'Company.name'
        db.add_column(u'home_company', 'name',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=255),
                      keep_default=False)

        # Adding field 'Company.phone'
        db.add_column(u'home_company', 'phone',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=255),
                      keep_default=False)

        # Adding field 'Company.fax'
        db.add_column(u'home_company', 'fax',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=255),
                      keep_default=False)

        # Adding field 'Company.email'
        db.add_column(u'home_company', 'email',
                      self.gf('django.db.models.fields.EmailField')(default=2, max_length=75),
                      keep_default=False)

        # Adding field 'Company.address'
        db.add_column(u'home_company', 'address',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=300),
                      keep_default=False)

        # Adding field 'Company.msg'
        db.add_column(u'home_company', 'msg',
                      self.gf('django.db.models.fields.TextField')(default=2),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Company.company_phone'
        db.add_column(u'home_company', 'company_phone',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=255),
                      keep_default=False)

        # Adding field 'Company.company_fax'
        db.add_column(u'home_company', 'company_fax',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=255),
                      keep_default=False)

        # Adding field 'Company.company_name'
        db.add_column(u'home_company', 'company_name',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=255),
                      keep_default=False)

        # Adding field 'Company.company_address'
        db.add_column(u'home_company', 'company_address',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=300),
                      keep_default=False)

        # Adding field 'Company.company_msg'
        db.add_column(u'home_company', 'company_msg',
                      self.gf('django.db.models.fields.TextField')(default=2),
                      keep_default=False)

        # Adding field 'Company.company_email'
        db.add_column(u'home_company', 'company_email',
                      self.gf('django.db.models.fields.EmailField')(default=2, max_length=75),
                      keep_default=False)

        # Deleting field 'Company.name'
        db.delete_column(u'home_company', 'name')

        # Deleting field 'Company.phone'
        db.delete_column(u'home_company', 'phone')

        # Deleting field 'Company.fax'
        db.delete_column(u'home_company', 'fax')

        # Deleting field 'Company.email'
        db.delete_column(u'home_company', 'email')

        # Deleting field 'Company.address'
        db.delete_column(u'home_company', 'address')

        # Deleting field 'Company.msg'
        db.delete_column(u'home_company', 'msg')


    models = {
        u'home.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msg': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['home']