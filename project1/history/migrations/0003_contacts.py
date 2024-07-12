# Generated by Django 5.0.3 on 2024-03-16 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_rename_facts_historical_data_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Email', models.EmailField(max_length=254)),
                ('Comment', models.TextField()),
            ],
        ),
    ]
