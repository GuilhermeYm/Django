# Generated by Django 5.0 on 2023-12-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("create_at", models.DateField(auto_now_add=True)),
                ("dead_line", models.DateTimeField()),
                ("finshed_at", models.DateTimeField(null=True)),
            ],
        ),
    ]