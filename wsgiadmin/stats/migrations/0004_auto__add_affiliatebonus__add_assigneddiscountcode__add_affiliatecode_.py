# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AffiliateBonus'
        db.create_table(u'stats_affiliatebonus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('base_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='affiliate_bonus_base_set', to=orm['auth.User'])),
            ('donor_user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='affiliate_bonus_donor', unique=True, to=orm['auth.User'])),
            ('affiliate_code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.AffiliateCode'])),
            ('counter', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('valid', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'stats', ['AffiliateBonus'])

        # Adding model 'AssignedDiscountCode'
        db.create_table(u'stats_assigneddiscountcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('discount_code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.DiscountCodes'])),
            ('valid', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'stats', ['AssignedDiscountCode'])

        # Adding model 'AffiliateCode'
        db.create_table(u'stats_affiliatecode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('code_type', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('value', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('valid', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'stats', ['AffiliateCode'])

        # Adding model 'DiscountCodes'
        db.create_table(u'stats_discountcodes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('code_type', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('value', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('valid', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'stats', ['DiscountCodes'])


    def backwards(self, orm):
        # Deleting model 'AffiliateBonus'
        db.delete_table(u'stats_affiliatebonus')

        # Deleting model 'AssignedDiscountCode'
        db.delete_table(u'stats_assigneddiscountcode')

        # Deleting model 'AffiliateCode'
        db.delete_table(u'stats_affiliatecode')

        # Deleting model 'DiscountCodes'
        db.delete_table(u'stats_discountcodes')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'clients.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'company_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'removed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'vat_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'stats.affiliatebonus': {
            'Meta': {'object_name': 'AffiliateBonus'},
            'affiliate_code': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.AffiliateCode']"}),
            'base_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'affiliate_bonus_base_set'", 'to': u"orm['auth.User']"}),
            'counter': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'donor_user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'affiliate_bonus_donor'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'stats.affiliatecode': {
            'Meta': {'object_name': 'AffiliateCode'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'code_type': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'value': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        },
        u'stats.assigneddiscountcode': {
            'Meta': {'object_name': 'AssignedDiscountCode'},
            'discount_code': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.DiscountCodes']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'stats.credit': {
            'Meta': {'object_name': 'Credit'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clients.Address']", 'null': 'True', 'blank': 'True'}),
            'bonus': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_payed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'stats.discountcodes': {
            'Meta': {'object_name': 'DiscountCodes'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'code_type': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'value': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        },
        u'stats.record': {
            'Meta': {'object_name': 'Record'},
            'cost': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'stats.transid': {
            'Meta': {'object_name': 'TransId'},
            'credit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.Credit']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'trans_id': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['stats']