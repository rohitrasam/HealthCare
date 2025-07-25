# Generated by Django 5.2.3 on 2025-06-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('specialization', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
            ],
        ),
    ]
