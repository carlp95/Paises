# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('L4', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciudad',
            old_name='Ciudad_pais',
            new_name='Codigo',
        ),
    ]
