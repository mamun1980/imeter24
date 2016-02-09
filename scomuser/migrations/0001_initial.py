# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ScomUserProfile'
        db.create_table(u'scomuser_scomuserprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('address_3', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('postal', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('home_phone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('cell_phone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('other_phone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('internal_extension', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('em_contact_1', self.gf('django.db.models.fields.TextField')(max_length=128, null=True, blank=True)),
            ('em_contact_2', self.gf('django.db.models.fields.TextField')(max_length=128, null=True, blank=True)),
            ('max_amount_allowed_to_purchase', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('max_purchase_per_po', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('search_string', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'scomuser', ['ScomUserProfile'])

        # Adding model 'Department'
        db.create_table(u'scomuser_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'scomuser', ['Department'])

        # Adding model 'PayType'
        db.create_table(u'scomuser_paytype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pay_type', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'scomuser', ['PayType'])

        # Adding model 'Payroll'
        db.create_table(u'scomuser_payroll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('sin', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('inital', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scomuser.Department'], null=True, blank=True)),
            ('rate_of_pay', self.gf('django.db.models.fields.DecimalField')(default='0.00', max_digits=10, decimal_places=2)),
            ('rate_of_pay_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scomuser.PayType'], null=True, blank=True)),
        ))
        db.send_create_signal(u'scomuser', ['Payroll'])

        # Adding model 'MassMail'
        db.create_table(u'scomuser_massmail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_id', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sender', self.gf('django.db.models.fields.EmailField')(max_length=100, null=True, blank=True)),
            ('to_all_users', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('reciever', self.gf('django.db.models.fields.EmailField')(max_length=100, null=True, blank=True)),
            ('mail_status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('request_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('delivered_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('search_string', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'scomuser', ['MassMail'])


    def backwards(self, orm):
        # Deleting model 'ScomUserProfile'
        db.delete_table(u'scomuser_scomuserprofile')

        # Deleting model 'Department'
        db.delete_table(u'scomuser_department')

        # Deleting model 'PayType'
        db.delete_table(u'scomuser_paytype')

        # Deleting model 'Payroll'
        db.delete_table(u'scomuser_payroll')

        # Deleting model 'MassMail'
        db.delete_table(u'scomuser_massmail')


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
        u'scomuser.massmail': {
            'Meta': {'object_name': 'MassMail'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'delivered_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'email_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'reciever': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'request_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'search_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sender': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'to_all_users': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'scomuser.payroll': {
            'Meta': {'object_name': 'Payroll'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scomuser.Department']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inital': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'rate_of_pay': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '10', 'decimal_places': '2'}),
            'rate_of_pay_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scomuser.PayType']", 'null': 'True', 'blank': 'True'}),
            'sin': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
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
            'internal_extension': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'max_amount_allowed_to_purchase': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'max_purchase_per_po': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'other_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'postal': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['scomuser']