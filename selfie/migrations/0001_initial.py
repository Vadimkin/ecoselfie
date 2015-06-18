# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Selfie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('selfie_before', models.ImageField(upload_to=b'', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f \xd0\xb4\xd0\xbe', blank=True)),
                ('selfie_after', models.ImageField(upload_to=b'', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f \xd0\xbf\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb5', blank=True)),
                ('balls', models.IntegerField(default=0, verbose_name=b'\xd0\x9e\xd1\x86\xd0\xb5\xd0\xbd\xd0\xba\xd0\xb0')),
                ('is_rated', models.BooleanField(default=False, verbose_name=b'\xd0\x95\xd1\x81\xd1\x82\xd1\x8c \xd0\xbb\xd0\xb8 \xd0\xbe\xd1\x86\xd0\xb5\xd0\xbd\xd0\xba\xd0\xb0')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb4\xd0\xbe\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('date_rated', models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x86\xd0\xb5\xd0\xbd\xd0\xba\xd0\xb8', blank=True)),
                ('user', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
