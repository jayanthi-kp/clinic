# Generated by Django 5.0 on 2023-12-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0006_alter_booking_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.TextField(db_column='status', null=True),
        ),
    ]
