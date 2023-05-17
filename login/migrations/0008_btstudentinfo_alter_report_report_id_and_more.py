# Generated by Django 4.1.7 on 2023-05-03 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0007_alter_report_report_id_delete_advisor"),
    ]

    operations = [
        migrations.CreateModel(
            name="BTStudentInfo",
            fields=[
                ("RegNo", models.IntegerField(primary_key=True, serialize=False)),
                ("RollNo", models.IntegerField()),
                ("Name", models.CharField(max_length=255)),
                ("Regulation", models.FloatField()),
                ("Dept", models.IntegerField()),
                ("AdmissionYear", models.IntegerField()),
                ("Gender", models.CharField(max_length=10)),
                ("Category", models.CharField(max_length=30)),
                ("GuardianName", models.CharField(max_length=255)),
                ("Phone", models.TextField()),
                ("email", models.TextField()),
                ("Address1", models.TextField()),
                ("Address2", models.TextField(null=True)),
                (
                    "Cycle",
                    models.IntegerField(
                        choices=[(10, "PHYSICS"), (9, "CHEMISTRY")], default=0
                    ),
                ),
            ],
            options={
                "db_table": "BTStudentInfo",
                "managed": True,
            },
        ),
        migrations.AlterField(
            model_name="report",
            name="report_id",
            field=models.CharField(
                default=datetime.datetime(2023, 5, 4, 1, 16, 35, 414060),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AddConstraint(
            model_name="btstudentinfo",
            constraint=models.UniqueConstraint(
                fields=("RegNo",), name="unique_BTStudentInfo_RegNo"
            ),
        ),
        migrations.AddConstraint(
            model_name="btstudentinfo",
            constraint=models.UniqueConstraint(
                fields=("RollNo",), name="unique_BTStudentInfo_RollNo"
            ),
        ),
    ]