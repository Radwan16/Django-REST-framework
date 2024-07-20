# Generated by Django 5.0.6 on 2024-07-20 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=32)),
                ('opis', models.TextField(max_length=256)),
                ('po_premierze', models.BooleanField(default=False)),
            ],
        ),
    ]
