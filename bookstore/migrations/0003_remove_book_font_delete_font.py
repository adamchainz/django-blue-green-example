# Generated by Django 4.2.5 on 2023-09-21 10:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bookstore", "0002_book_price"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            # Operations in the project state.
            state_operations=[
                migrations.RemoveField(
                    model_name="book",
                    name="font",
                ),
                migrations.DeleteModel(
                    name="Font",
                ),
            ],
            # No changes in the database.
            database_operations=[],
        ),
    ]
