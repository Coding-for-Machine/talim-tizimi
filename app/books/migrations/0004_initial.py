# Generated by Django 5.1.7 on 2025-03-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("books", "0003_delete_books"),
    ]

    operations = [
        migrations.CreateModel(
            name="Books",
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
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(db_index=True, max_length=250)),
                ("body", models.TextField(db_index=True)),
                ("images", models.ImageField(upload_to="booksimage/")),
                ("books_pdf", models.FileField(upload_to="bookspdf/")),
            ],
            options={
                "ordering": ["-updated_at"],
            },
        ),
    ]
