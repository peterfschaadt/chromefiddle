# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Platforms'
        db.delete_table('flags_platforms')

        # Adding field 'Flag.is_mac'
        db.add_column('flags_flag', 'is_mac',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Flag.is_windows'
        db.add_column('flags_flag', 'is_windows',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Flag.is_linux'
        db.add_column('flags_flag', 'is_linux',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Flag.is_chrome_os'
        db.add_column('flags_flag', 'is_chrome_os',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Flag.is_android'
        db.add_column('flags_flag', 'is_android',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Removing M2M table for field compatibility on 'Flag'
        db.delete_table('flags_flag_compatibility')


    def backwards(self, orm):
        # Adding model 'Platforms'
        db.create_table('flags_platforms', (
            ('support', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('flags', ['Platforms'])

        # Deleting field 'Flag.is_mac'
        db.delete_column('flags_flag', 'is_mac')

        # Deleting field 'Flag.is_windows'
        db.delete_column('flags_flag', 'is_windows')

        # Deleting field 'Flag.is_linux'
        db.delete_column('flags_flag', 'is_linux')

        # Deleting field 'Flag.is_chrome_os'
        db.delete_column('flags_flag', 'is_chrome_os')

        # Deleting field 'Flag.is_android'
        db.delete_column('flags_flag', 'is_android')

        # Adding M2M table for field compatibility on 'Flag'
        db.create_table('flags_flag_compatibility', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('flag', models.ForeignKey(orm['flags.flag'], null=False)),
            ('platforms', models.ForeignKey(orm['flags.platforms'], null=False))
        ))
        db.create_unique('flags_flag_compatibility', ['flag_id', 'platforms_id'])


    models = {
        'flags.flag': {
            'Meta': {'object_name': 'Flag'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_android': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_chrome_os': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_linux': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_mac': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_windows': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['flags']