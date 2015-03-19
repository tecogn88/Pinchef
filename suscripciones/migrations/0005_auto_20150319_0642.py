# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suscripciones', '0004_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('movimiento', models.CharField(max_length=55)),
                ('suscripcion', models.ForeignKey(related_name='movimientos', to='suscripciones.Suscripcion')),
            ],
            options={
                'verbose_name': 'Historial',
                'verbose_name_plural': 'Historial',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='log',
            name='suscripcion',
        ),
        migrations.DeleteModel(
            name='Log',
        ),
    ]
