# Generated by Django 5.0 on 2024-01-03 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password_generator', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
