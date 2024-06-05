# Generated by Django 5.0.6 on 2024-06-04 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conscript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FitnessForService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=2)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MilitaryCommissariat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MilitaryRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_series', models.CharField(max_length=4)),
                ('passport_number', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalExamination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examination_date', models.DateField()),
                ('health_notes', models.TextField()),
                ('conscript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='military_commissariat.conscript')),
                ('fitness_for_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='military_commissariat.fitnessforservice')),
            ],
        ),
        migrations.CreateModel(
            name='Official',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('military_commissariat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='military_commissariat.militarycommissariat')),
            ],
        ),
        migrations.CreateModel(
            name='MilitaryID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_date', models.DateField()),
                ('characteristic', models.CharField(max_length=200)),
                ('conscript', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='military_commissariat.conscript')),
                ('fitness_for_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='military_commissariat.fitnessforservice')),
                ('assigned_rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='military_commissariat.militaryrank')),
                ('official', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='military_commissariat.official')),
            ],
        ),
        migrations.AddField(
            model_name='conscript',
            name='personal_data',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='military_commissariat.personaldata'),
        ),
        migrations.CreateModel(
            name='Summon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appearance_date', models.DateField()),
                ('appearance_time', models.TimeField()),
                ('appearance_location', models.CharField(max_length=100)),
                ('reason', models.TextField()),
                ('issued_date', models.DateField()),
                ('conscript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='military_commissariat.conscript')),
                ('official', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='military_commissariat.official')),
            ],
        ),
    ]
