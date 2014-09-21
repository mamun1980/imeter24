# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Department'
        db.create_table(u'scomuser_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'scomuser', ['Department'])

        # Adding model 'Payroll'
        db.create_table(u'scomuser_payroll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('sin', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('inital', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scomuser.Department'], null=True, blank=True)),
            ('rate_of_pay', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('rate_of_pay_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scomuser.PayType'], null=True, blank=True)),
        ))
        db.send_create_signal(u'scomuser', ['Payroll'])

        # Adding model 'PayType'
        db.create_table(u'scomuser_paytype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pay_type', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'scomuser', ['PayType'])

        # Adding field 'ScomUserProfile.address_1'
        db.add_column(u'scomuser_scomuserprofile', 'address_1',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScomUserProfile.address_2'
        db.add_column(u'scomuser_scomuserprofile', 'address_2',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScomUserProfile.address_3'
        db.add_column(u'scomuser_scomuserprofile', 'address_3',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScomUserProfile.city'
        db.add_column(u'scomuser_scomuserprofile', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScomUserProfile.province'
        db.add_column(u'scomuser_scomuserprofile', 'province',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScomUserProfile.postal'
        db.add_column(u'scomuser_scomuserprofile', 'postal',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScomUserProfile.home_phone'
        db.add_column(u'scomuser_scomuserprofile', 'home_phone',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScomUserProfile.cell_phone'
        db.add_column(u'scomuser_scomuserprofile', 'cell_phone',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScomUserProfile.other_phone'
        db.add_column(u'scomuser_scomuserprofile', 'other_phone',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScomUserProfile.em_contact_1'
        db.add_column(u'scomuser_scomuserprofile', 'em_contact_1',
                      self.gf('django.db.models.fields.TextField')(max_length=128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScomUserProfile.em_contact_2'
        db.add_column(u'scomuser_scomuserprofile', 'em_contact_2',
                      self.gf('django.db.models.fields.TextField')(max_length=128, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Department'
        db.delete_table(u'scomuser_department')

        # Deleting model 'Payroll'
        db.delete_table(u'scomuser_payroll')

        # Deleting model 'PayType'
        db.delete_table(u'scomuser_paytype')

        # Deleting field 'ScomUserProfile.address_1'
        db.delete_column(u'scomuser_scomuserprofile', 'address_1')

        # Deleting field 'ScomUserProfile.address_2'
        db.delete_column(u'scomuser_scomuserprofile', 'address_2')

        # Deleting field 'ScomUserProfile.address_3'
        db.delete_column(u'scomuser_scomuserprofile', 'address_3')

        # Deleting field 'ScomUserProfile.city'
        db.delete_column(u'scomuser_scomuserprofile', 'city')

        # Deleting field 'ScomUserProfile.province'
        db.delete_column(u'scomuser_scomuserprofile', 'province')

        # Deleting field 'ScomUserProfile.postal'
        db.delete_column(u'scomuser_scomuserprofile', 'postal')

        # Deleting field 'ScomUserProfile.home_phone'
        db.delete_column(u'scomuser_scomuserprofile', 'home_phone')

        # Deleting field 'ScomUserProfile.cell_phone'
        db.delete_column(u'scomuser_scomuserprofile', 'cell_phone')

        # Deleting field 'ScomUserProfile.other_phone'
        db.delete_column(u'scomuser_scomuserprofile', 'other_phone')

        # Deleting field 'ScomUserProfile.em_contact_1'
        db.delete_column(u'scomuser_scomuserprofile', 'em_contact_1')

        # Deleting field 'ScomUserProfile.em_contact_2'
        db.delete_column(u'scomuser_scomuserprofile', 'em_contact_2')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'scomuser.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'scomuser.payroll': {
            'Meta': {'object_name': 'Payroll'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scomuser.Department']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inital': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'rate_of_pay': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'rate_of_pay_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scomuser.PayType']", 'null': 'True', 'blank': 'True'}),
            'sin': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'scomuser.paytype': {
            'Meta': {'object_name': 'PayType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pay_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'scomuser.scomuserprofile': {
            'Meta': {'object_name': 'ScomUserProfile'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'address_3': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cell_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'em_contact_1': ('django.db.models.fields.TextField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'em_contact_2': ('django.db.models.fields.TextField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'postal': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['scomuser']