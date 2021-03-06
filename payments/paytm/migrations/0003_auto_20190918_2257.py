# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-09-18 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('paytm', '0002_auto_20170309_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='paytmhistory',
            name='CHECKSUMHASH',
            field=models.CharField(blank=True, max_length=110, null=True, verbose_name=b'CHECKSUMHASH'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='BANKNAME',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name=b'BANKNAME'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='BANKTXNID',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=b'BANKTXNID'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='CURRENCY',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name=b'CURRENCY'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='GATEWAYNAME',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name=b'GATEWAYNAME'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='ORDERID',
            field=models.CharField(max_length=100, verbose_name=b'ORDERID'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='PAYMENTMODE',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name=b'PAYMENTMODE'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='RESPCODE',
            field=models.IntegerField(verbose_name=b'RESPCODE'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='RESPMSG',
            field=models.TextField(max_length=500, verbose_name=b'RESPMSG'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='STATUS',
            field=models.CharField(max_length=50, verbose_name=b'STATUS'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='TXNAMOUNT',
            field=models.FloatField(verbose_name=b'TXNAMOUNT'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='TXNDATE',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'TXNDATE'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='TXNID',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=b'TXNID'),
        ),
    ]
