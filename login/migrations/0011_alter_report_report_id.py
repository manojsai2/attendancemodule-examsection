# Generated by Django 4.1.7 on 2023-05-03 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0010_alter_report_report_id_btcourses_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="report_id",
            field=models.CharField(
                default=datetime.datetime(2023, 5, 4, 1, 25, 49, 519410),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
