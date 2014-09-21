# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DistributionMethod'
        db.create_table(u'contacts_distributionmethod', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('distribution_method', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'contacts', ['DistributionMethod'])

        # Adding model 'DeliveryChoice'
        db.create_table(u'contacts_deliverychoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('delivery_choice', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'contacts', ['DeliveryChoice'])

        # Adding model 'PaymentTerm'
        db.create_table(u'contacts_paymentterm', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'contacts', ['PaymentTerm'])

        # Adding model 'Currency'
        db.create_table(u'contacts_currency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['Currency'])

        # Adding model 'Contact'
        db.create_table(u'contacts_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('attention_to', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('province', self.gf('django.db.models.fields.CharField')(default='Ontario', max_length=64, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(default='Canada', max_length=40, null=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('webpage', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['Contact'])

        # Adding model 'ContactProfile'
        db.create_table(u'contacts_contactprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contacts.Contact'], unique=True)),
            ('gst_number', self.gf('django.db.models.fields.CharField')(max_length=17, null=True, blank=True)),
            ('gst_tax_exempt', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hst_number', self.gf('django.db.models.fields.CharField')(max_length=17, null=True, blank=True)),
            ('hst_tax_exempt', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pst_number', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('pst_tax_exempt', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('foreign_account', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('mail_list', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('terms', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.PaymentTerm'], null=True, blank=True)),
            ('shipping_method', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.DeliveryChoice'], null=True, blank=True)),
            ('ship_collect', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Currency'], null=True, blank=True)),
            ('fob', self.gf('django.db.models.fields.CharField')(default='Oshawa, Ontario, Canada', max_length=50, null=True, blank=True)),
            ('ap_contact', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('bv_ap_account', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('bv_ar_account', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('record_created', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_activity', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['ContactProfile'])

        # Adding model 'PhoneType'
        db.create_table(u'contacts_phonetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_type', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['PhoneType'])

        # Adding model 'ContactPhone'
        db.create_table(u'contacts_contactphone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'])),
            ('phone_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.PhoneType'], null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('phone_ext', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['ContactPhone'])

        # Adding model 'ContactType'
        db.create_table(u'contacts_contacttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact_type', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'contacts', ['ContactType'])

        # Adding model 'ContactContactType'
        db.create_table(u'contacts_contactcontacttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'])),
            ('contact_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.ContactType'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['ContactContactType'])

        # Adding model 'EmailAddressType'
        db.create_table(u'contacts_emailaddresstype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_type', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'contacts', ['EmailAddressType'])

        # Adding model 'ContactEmailAddress'
        db.create_table(u'contacts_contactemailaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'])),
            ('email_address_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.EmailAddressType'])),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=100)),
        ))
        db.send_create_signal(u'contacts', ['ContactEmailAddress'])

        # Adding model 'ContactDistributionMethod'
        db.create_table(u'contacts_contactdistributionmethod', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('distribution_method', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.DistributionMethod'])),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['ContactDistributionMethod'])

        # Adding model 'Comment'
        db.create_table(u'contacts_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'])),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('comment_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'DistributionMethod'
        db.delete_table(u'contacts_distributionmethod')

        # Deleting model 'DeliveryChoice'
        db.delete_table(u'contacts_deliverychoice')

        # Deleting model 'PaymentTerm'
        db.delete_table(u'contacts_paymentterm')

        # Deleting model 'Currency'
        db.delete_table(u'contacts_currency')

        # Deleting model 'Contact'
        db.delete_table(u'contacts_contact')

        # Deleting model 'ContactProfile'
        db.delete_table(u'contacts_contactprofile')

        # Deleting model 'PhoneType'
        db.delete_table(u'contacts_phonetype')

        # Deleting model 'ContactPhone'
        db.delete_table(u'contacts_contactphone')

        # Deleting model 'ContactType'
        db.delete_table(u'contacts_contacttype')

        # Deleting model 'ContactContactType'
        db.delete_table(u'contacts_contactcontacttype')

        # Deleting model 'EmailAddressType'
        db.delete_table(u'contacts_emailaddresstype')

        # Deleting model 'ContactEmailAddress'
        db.delete_table(u'contacts_contactemailaddress')

        # Deleting model 'ContactDistributionMethod'
        db.delete_table(u'contacts_contactdistributionmethod')

        # Deleting model 'Comment'
        db.delete_table(u'contacts_comment')


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
        u'contacts.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comment_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'attention_to': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Canada'", 'max_length': '40', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'default': "'Ontario'", 'max_length': '64', 'blank': 'True'}),
            'webpage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'contacts.contactcontacttype': {
            'Meta': {'object_name': 'ContactContactType'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            'contact_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.ContactType']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.contactdistributionmethod': {
            'Meta': {'object_name': 'ContactDistributionMethod'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'distribution_method': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.DistributionMethod']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.contactemailaddress': {
            'Meta': {'object_name': 'ContactEmailAddress'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'email_address_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.EmailAddressType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.contactphone': {
            'Meta': {'object_name': 'ContactPhone'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'phone_ext': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'phone_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.PhoneType']", 'null': 'True', 'blank': 'True'})
        },
        u'contacts.contactprofile': {
            'Meta': {'object_name': 'ContactProfile'},
            'ap_contact': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bv_ap_account': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'bv_ar_account': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contacts.Contact']", 'unique': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Currency']", 'null': 'True', 'blank': 'True'}),
            'fob': ('django.db.models.fields.CharField', [], {'default': "'Oshawa, Ontario, Canada'", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'foreign_account': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'gst_number': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'gst_tax_exempt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hst_number': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'hst_tax_exempt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_activity': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'mail_list': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'pst_number': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'pst_tax_exempt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'record_created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ship_collect': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shipping_method': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.DeliveryChoice']", 'null': 'True', 'blank': 'True'}),
            'terms': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.PaymentTerm']", 'null': 'True', 'blank': 'True'})
        },
        u'contacts.contacttype': {
            'Meta': {'object_name': 'ContactType'},
            'contact_type': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'contacts.currency': {
            'Meta': {'object_name': 'Currency'},
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.deliverychoice': {
            'Meta': {'object_name': 'DeliveryChoice'},
            'delivery_choice': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'contacts.distributionmethod': {
            'Meta': {'object_name': 'DistributionMethod'},
            'distribution_method': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'contacts.emailaddresstype': {
            'Meta': {'object_name': 'EmailAddressType'},
            'email_type': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'contacts.paymentterm': {
            'Meta': {'object_name': 'PaymentTerm'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        },
        u'contacts.phonetype': {
            'Meta': {'object_name': 'PhoneType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contacts']