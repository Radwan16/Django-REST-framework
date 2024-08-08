# Generated by Django 5.0.6 on 2024-08-08 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_extrainfo_film_extra_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(2, 'Sci-fi'), (1, 'Horror'), (3, 'Drama'), (4, 'Komedia'), (0, 'Nieznane')], default=0),
        ),
        migrations.CreateModel(
            name='Recenzja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis', models.TextField(default='')),
                ('gwiazdki', models.IntegerField(default=5)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.film')),
            ],
        ),
    ]