# Generated by Django 4.1.7 on 2023-05-03 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0011_alter_report_report_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="BTRegistrationStatus",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("AYear", models.IntegerField()),
                ("ASem", models.IntegerField()),
                ("BYear", models.IntegerField()),
                ("BSem", models.IntegerField()),
                ("Regulation", models.FloatField()),
                ("Dept", models.IntegerField()),
                ("Mode", models.CharField(max_length=1)),
                ("Status", models.IntegerField()),
                ("RollListStatus", models.IntegerField()),
                ("RollListFeeStatus", models.IntegerField()),
                ("OERollListStatus", models.IntegerField()),
                ("OERegistrationStatus", models.IntegerField()),
                ("RegistrationStatus", models.IntegerField()),
                ("MarksStatus", models.IntegerField()),
                ("GradeStatus", models.IntegerField()),
            ],
            options={
                "db_table": "BTRegistration_Status",
                "managed": True,
            },
        ),
        migrations.AlterField(
            model_name="report",
            name="report_id",
            field=models.CharField(
                default=datetime.datetime(2023, 5, 4, 1, 26, 4, 606479),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AddConstraint(
            model_name="btregistrationstatus",
            constraint=models.UniqueConstraint(
                fields=("AYear", "ASem", "BYear", "BSem", "Regulation", "Dept", "Mode"),
                name="unique_BTRegistrationstatus",
            ),
        ),
    ]