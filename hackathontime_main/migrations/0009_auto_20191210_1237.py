# Generated by Django 2.2.7 on 2019-12-10 07:07

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hackathontime_main', '0008_auto_20191210_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hackathon',
            name='hackathon_location_name',
        ),
        migrations.RemoveField(
            model_name='hackathon',
            name='hackathon_location_url',
        ),
        migrations.AddField(
            model_name='hackathon',
            name='hackathon_address',
            field=django_google_maps.fields.AddressField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='hackathon_geolocation',
            field=django_google_maps.fields.GeoLocationField(blank=True, max_length=100),
        ),
    ]
