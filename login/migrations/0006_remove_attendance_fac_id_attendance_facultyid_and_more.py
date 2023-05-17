# Generated by Django 4.1.7 on 2023-05-03 19:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0005_remove_btfacultyinfo_id_remove_report_fac_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="attendance",
            name="fac_id",
        ),
        migrations.AddField(
            model_name="attendance",
            name="FacultyId",
            field=models.ForeignKey(
                default=100,
                on_delete=django.db.models.deletion.CASCADE,
                to="login.btfacultyinfo",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="report",
            name="report_id",
            field=models.CharField(
                default=datetime.datetime(2023, 5, 4, 1, 10, 38, 638819),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]