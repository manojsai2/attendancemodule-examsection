# Generated by Django 4.1.7 on 2023-05-03 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0003_alter_report_report_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="BTFacultyInfo",
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
                ("FacultyId", models.IntegerField(default=100)),
                ("f_password", models.CharField(max_length=30)),
                ("Name", models.CharField(max_length=255)),
                ("Phone", models.TextField()),
                ("Email", models.CharField(max_length=255)),
                ("Dept", models.IntegerField()),
                ("Working", models.BooleanField()),
            ],
            options={
                "db_table": "BTFacultyInfo",
                "managed": True,
            },
        ),
        migrations.AlterField(
            model_name="report",
            name="report_id",
            field=models.CharField(
                default=datetime.datetime(2023, 5, 4, 0, 41, 13, 592064),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AddConstraint(
            model_name="btfacultyinfo",
            constraint=models.UniqueConstraint(
                fields=("FacultyId",), name="unique_BTfacultyinfo_facultyid"
            ),
        ),
    ]
