# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('L4', '0002_auto_20151125_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciudad',
            old_name='Codigo',
            new_name='Ciudad_pais',
        ),
    ]
