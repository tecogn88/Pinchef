# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_remove_usuario_birthdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferencias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('res', models.IntegerField(max_length=11)),
                ('cerdo', models.IntegerField(max_length=11)),
                ('pollo', models.IntegerField(max_length=11)),
                ('pescado', models.IntegerField(max_length=11)),
                ('mariscos', models.IntegerField(max_length=11)),
                ('cordero', models.IntegerField(max_length=11)),
                ('alimentacion', models.IntegerField(max_length=11)),
                ('restriccion', models.TextField(blank=True)),
                ('usuario', models.ForeignKey(to='usuarios.Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
