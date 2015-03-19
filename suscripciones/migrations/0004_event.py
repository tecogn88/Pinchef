# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suscripciones', '0003_auto_20150319_0429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('id_evento', models.CharField(max_length=25)),
                ('objeto', models.CharField(max_length=25)),
                ('livemode', models.BooleanField()),
                ('created_at', models.CharField(max_length=25)),
                ('event_type', models.CharField(max_length=25)),
                ('data', models.TextField()),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
            bases=(models.Model,),
        ),
    ]
