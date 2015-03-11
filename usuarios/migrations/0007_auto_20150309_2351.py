# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_preferencias'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Preferencias',
            new_name='Preferencia',
        ),
    ]
