# Generated by Django 4.1.4 on 2022-12-22 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, choices=[('Electronics', 'Electronics'), ('Books', 'Books'), ('Food', 'Food')], max_length=255, null=True)),
                ('quantity', models.PositiveBigIntegerField(blank=True, null=True)),
            ],
        ),
    ]