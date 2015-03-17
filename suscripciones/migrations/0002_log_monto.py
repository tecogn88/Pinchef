# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suscripciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='monto',
            field=models.FloatField(default=100.0),
            preserve_default=False,
        ),
    ]
