# Generated by Django 4.0.5 on 2022-06-13 07:19

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoapi', '0007_alter_geolocation_geo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geolocation',
            name='geo',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
