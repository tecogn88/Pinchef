# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('suscripciones', '0002_log_monto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscripcion',
            name='usuario',
            field=models.ForeignKey(related_name='suscripciones', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
