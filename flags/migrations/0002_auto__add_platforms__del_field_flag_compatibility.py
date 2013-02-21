# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Platforms'
        db.create_table('flags_platforms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('support', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('flags', ['Platforms'])

        # Deleting field 'Flag.compatibility'
        db.delete_column('flags_flag', 'compatibility')

        # Adding M2M table for field compatibility on 'Flag'
        db.create_table('flags_flag_compatibility', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('flag', models.ForeignKey(orm['flags.flag'], null=False)),
            ('platforms', models.ForeignKey(orm['flags.platforms'], null=False))
        ))
        db.create_unique('flags_flag_compatibility', ['flag_id', 'platforms_id'])


    def backwards(self, orm):
        # Deleting model 'Platforms'
        db.delete_table('flags_platforms')

        # Adding field 'Flag.compatibility'
        db.add_column('flags_flag', 'compatibility',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)

        # Removing M2M table for field compatibility on 'Flag'
        db.delete_table('flags_flag_compatibility')


    models = {
        'flags.flag': {
            'Meta': {'object_name': 'Flag'},
            'compatibility': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['flags.Platforms']", 'symmetrical': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'flags.platforms': {
            'Meta': {'object_name': 'Platforms'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'support': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['flags']