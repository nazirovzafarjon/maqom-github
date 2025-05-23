# Generated by Django 5.1.3 on 2024-11-19 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaqomlarTuri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tur_nomi', models.CharField(max_length=255, verbose_name='Maqom turi')),
            ],
            options={
                'db_table': 'MaqomlarTuri',
            },
        ),
        migrations.CreateModel(
            name='MaqomlarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqom_nomi', models.CharField(max_length=355, verbose_name='Maqom nomi')),
                ('ijrochi_surati', models.ImageField(upload_to='media/', verbose_name='Ijrochi surati')),
                ('maqom_sozlari', models.TextField(verbose_name="Maqom so'zlari")),
                ('maqom_yartuvchisi', models.CharField(max_length=355, verbose_name='Maqom yaratuvchisi')),
                ('maqom_ijrochisi', models.CharField(max_length=355, verbose_name='Maqom ijrochisi')),
                ('maqom_turi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maqomlar', to='home.maqomlarturi', verbose_name='Maqom turi')),
            ],
            options={
                'db_table': 'MaqomlarModel',
            },
        ),
    ]
