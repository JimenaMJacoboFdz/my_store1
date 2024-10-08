# Generated by Django 4.1 on 2024-10-02 19:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=50)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("sku", models.CharField(max_length=10)),
                ("category", models.CharField(max_length=50)),
                ("brand", models.CharField(max_length=50)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="media/products"
                    ),
                ),
                ("discount", models.IntegerField()),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("published_date", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
