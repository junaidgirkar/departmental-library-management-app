# Generated by Django 3.1.5 on 2021-01-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Account", "0003_student_sap_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="branch",
            new_name="department",
        ),
        migrations.RenameField(
            model_name="teacher",
            old_name="subject",
            new_name="department",
        ),
        migrations.RemoveField(
            model_name="user",
            name="date_joined",
        ),
        migrations.AddField(
            model_name="student",
            name="graduation_year",
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AddField(
            model_name="teacher",
            name="sap_id",
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name="user",
            name="address",
            field=models.CharField(blank=True, max_length=255, verbose_name="address"),
        ),
        migrations.AddField(
            model_name="user",
            name="mobile",
            field=models.CharField(blank=True, max_length=13, verbose_name="mobile"),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=40, verbose_name="first_name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(blank=True, max_length=40, verbose_name="last name"),
        ),
    ]
