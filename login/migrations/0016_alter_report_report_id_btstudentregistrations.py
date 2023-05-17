# Generated by Django 4.1.7 on 2023-05-04 08:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0015_alter_btsubjects_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="report_id",
            field=models.CharField(
                default=datetime.datetime(2023, 5, 4, 14, 1, 27, 147288),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.CreateModel(
            name="BTStudentRegistrations",
            fields=[
                ("RegId", models.IntegerField(primary_key=True, serialize=False)),
                ("Year", models.IntegerField()),
                (
                    "Student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="login.btstudentinfo",
                    ),
                ),
                (
                    "SubCode",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="login.btcourses",
                    ),
                ),
            ],
        ),
    ]
