# Generated by Django 5.0.2 on 2024-06-22 08:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('bus_id', models.AutoField(primary_key=True, serialize=False)),
                ('bus_name', models.CharField(max_length=50)),
                ('bus_number', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'bus',
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(default='default@example.com', max_length=225)),
                ('contact', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='passenger_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'passenger',
            },
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('pass_id', models.AutoField(primary_key=True, serialize=False)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passes', to='myapp.bus')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passes', to='myapp.passenger')),
            ],
            options={
                'db_table': 'pass',
            },
        ),
    ]