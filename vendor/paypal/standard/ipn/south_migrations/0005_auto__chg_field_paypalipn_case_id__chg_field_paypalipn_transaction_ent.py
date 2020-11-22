# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PayPalIPN.case_id'
        db.alter_column(u'paypal_ipn', 'case_id', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.transaction_entity'
        db.alter_column(u'paypal_ipn', 'transaction_entity', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.address_status'
        db.alter_column(u'paypal_ipn', 'address_status', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.reason_code'
        db.alter_column(u'paypal_ipn', 'reason_code', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.profile_status'
        db.alter_column(u'paypal_ipn', 'profile_status', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.txn_id'
        db.alter_column(u'paypal_ipn', 'txn_id', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.payment_status'
        db.alter_column(u'paypal_ipn', 'payment_status', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.payer_status'
        db.alter_column(u'paypal_ipn', 'payer_status', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.period_type'
        db.alter_column(u'paypal_ipn', 'period_type', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.pending_reason'
        db.alter_column(u'paypal_ipn', 'pending_reason', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.payment_type'
        db.alter_column(u'paypal_ipn', 'payment_type', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.recurring_payment_id'
        db.alter_column(u'paypal_ipn', 'recurring_payment_id', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.protection_eligibility'
        db.alter_column(u'paypal_ipn', 'protection_eligibility', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.receiver_email'
        db.alter_column(u'paypal_ipn', 'receiver_email', self.gf('django.db.models.fields.EmailField')(max_length=254))

        # Changing field 'PayPalIPN.txn_type'
        db.alter_column(u'paypal_ipn', 'txn_type', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.auth_status'
        db.alter_column(u'paypal_ipn', 'auth_status', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.payment_cycle'
        db.alter_column(u'paypal_ipn', 'payment_cycle', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.charset'
        db.alter_column(u'paypal_ipn', 'charset', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.product_name'
        db.alter_column(u'paypal_ipn', 'product_name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.receiver_id'
        db.alter_column(u'paypal_ipn', 'receiver_id', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.period2'
        db.alter_column(u'paypal_ipn', 'period2', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.period3'
        db.alter_column(u'paypal_ipn', 'period3', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.period1'
        db.alter_column(u'paypal_ipn', 'period1', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.product_type'
        db.alter_column(u'paypal_ipn', 'product_type', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.receipt_id'
        db.alter_column(u'paypal_ipn', 'receipt_id', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'PayPalIPN.case_type'
        db.alter_column(u'paypal_ipn', 'case_type', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'PayPalIPN.case_id'
        db.alter_column(u'paypal_ipn', 'case_id', self.gf('django.db.models.fields.CharField')(max_length=14))

        # Changing field 'PayPalIPN.transaction_entity'
        db.alter_column(u'paypal_ipn', 'transaction_entity', self.gf('django.db.models.fields.CharField')(max_length=7))

        # Changing field 'PayPalIPN.address_status'
        db.alter_column(u'paypal_ipn', 'address_status', self.gf('django.db.models.fields.CharField')(max_length=11))

        # Changing field 'PayPalIPN.reason_code'
        db.alter_column(u'paypal_ipn', 'reason_code', self.gf('django.db.models.fields.CharField')(max_length=15))

        # Changing field 'PayPalIPN.profile_status'
        db.alter_column(u'paypal_ipn', 'profile_status', self.gf('django.db.models.fields.CharField')(max_length=32))

        # Changing field 'PayPalIPN.txn_id'
        db.alter_column(u'paypal_ipn', 'txn_id', self.gf('django.db.models.fields.CharField')(max_length=19))

        # Changing field 'PayPalIPN.payment_status'
        db.alter_column(u'paypal_ipn', 'payment_status', self.gf('django.db.models.fields.CharField')(max_length=17))

        # Changing field 'PayPalIPN.payer_status'
        db.alter_column(u'paypal_ipn', 'payer_status', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'PayPalIPN.period_type'
        db.alter_column(u'paypal_ipn', 'period_type', self.gf('django.db.models.fields.CharField')(max_length=32))

        # Changing field 'PayPalIPN.pending_reason'
        db.alter_column(u'paypal_ipn', 'pending_reason', self.gf('django.db.models.fields.CharField')(max_length=14))

        # Changing field 'PayPalIPN.payment_type'
        db.alter_column(u'paypal_ipn', 'payment_type', self.gf('django.db.models.fields.CharField')(max_length=7))

        # Changing field 'PayPalIPN.recurring_payment_id'
        db.alter_column(u'paypal_ipn', 'recurring_payment_id', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'PayPalIPN.protection_eligibility'
        db.alter_column(u'paypal_ipn', 'protection_eligibility', self.gf('django.db.models.fields.CharField')(max_length=32))

        # Changing field 'PayPalIPN.receiver_email'
        db.alter_column(u'paypal_ipn', 'receiver_email', self.gf('django.db.models.fields.EmailField')(max_length=127))

        # Changing field 'PayPalIPN.txn_type'
        db.alter_column(u'paypal_ipn', 'txn_type', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'PayPalIPN.auth_status'
        db.alter_column(u'paypal_ipn', 'auth_status', self.gf('django.db.models.fields.CharField')(max_length=9))

        # Changing field 'PayPalIPN.payment_cycle'
        db.alter_column(u'paypal_ipn', 'payment_cycle', self.gf('django.db.models.fields.CharField')(max_length=32))

        # Changing field 'PayPalIPN.charset'
        db.alter_column(u'paypal_ipn', 'charset', self.gf('django.db.models.fields.CharField')(max_length=32))

        # Changing field 'PayPalIPN.product_name'
        db.alter_column(u'paypal_ipn', 'product_name', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'PayPalIPN.receiver_id'
        db.alter_column(u'paypal_ipn', 'receiver_id', self.gf('django.db.models.fields.CharField')(max_length=127))

        # Changing field 'PayPalIPN.period2'
        db.alter_column(u'paypal_ipn', 'period2', self.gf('django.db.models.fields.CharField')(max_length=32))

        # Changing field 'PayPalIPN.period3'
        db.alter_column(u'paypal_ipn', 'period3', self.gf('django.db.models.fields.CharField')(max_length=32))

        # Changing field 'PayPalIPN.period1'
        db.alter_column(u'paypal_ipn', 'period1', self.gf('django.db.models.fields.CharField')(max_length=32))

        # Changing field 'PayPalIPN.product_type'
        db.alter_column(u'paypal_ipn', 'product_type', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'PayPalIPN.receipt_id'
        db.alter_column(u'paypal_ipn', 'receipt_id', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'PayPalIPN.case_type'
        db.alter_column(u'paypal_ipn', 'case_type', self.gf('django.db.models.fields.CharField')(max_length=24))

    models = {
        u'ipn.paypalipn': {
            'Meta': {'object_name': 'PayPalIPN', 'db_table': "u'paypal_ipn'"},
            'address_city': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'address_country': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'address_country_code': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'address_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'address_state': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'address_status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'address_zip': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'amount1': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'amount2': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'amount3': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'amount_per_cycle': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'auction_buyer_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'auction_closing_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'auction_multi_item': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'auth_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'auth_exp': ('django.db.models.fields.CharField', [], {'max_length': '28', 'blank': 'True'}),
            'auth_id': ('django.db.models.fields.CharField', [], {'max_length': '19', 'blank': 'True'}),
            'auth_status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'business': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'case_creation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'case_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'case_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'charset': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency_code': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '32', 'blank': 'True'}),
            'custom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'exchange_rate': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '16', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flag_code': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'flag_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'for_auction': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'from_view': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'handling_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_payment_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'invoice': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'ipaddress': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'item_name': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'item_number': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'mc_amount1': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'mc_amount2': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'mc_amount3': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'mc_currency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '32', 'blank': 'True'}),
            'mc_fee': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'mc_gross': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'mc_handling': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'mc_shipping': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'memo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'mp_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'next_payment_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'notify_version': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'num_cart_items': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'option_name1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'option_name2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'outstanding_balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'parent_txn_id': ('django.db.models.fields.CharField', [], {'max_length': '19', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'payer_business_name': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'payer_email': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'payer_id': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'}),
            'payer_status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'payment_cycle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'payment_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'payment_gross': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'payment_status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'payment_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pending_reason': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'period1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'period2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'period3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'period_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'product_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'profile_status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'protection_eligibility': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'query': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'reason_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'reattempt': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'receipt_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'receiver_email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'receiver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'recur_times': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'recurring': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'recurring_payment_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'remaining_settle': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'residence_country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'response': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'retry_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'rp_invoice_id': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'settle_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'settle_currency': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'shipping': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'shipping_method': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'subscr_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'subscr_effective': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'subscr_id': ('django.db.models.fields.CharField', [], {'max_length': '19', 'blank': 'True'}),
            'tax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'test_ipn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'transaction_entity': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'transaction_subject': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'txn_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'txn_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'verify_sign': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['ipn']