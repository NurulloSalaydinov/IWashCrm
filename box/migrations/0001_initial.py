# Generated by Django 4.1.5 on 2023-05-19 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('token', models.SlugField(unique=True)),
                ('cash', models.PositiveIntegerField(default=0)),
                ('on', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turniket_id', models.CharField(max_length=16)),
                ('cash_back', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_used_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.PositiveIntegerField(default=27)),
                ('wax', models.PositiveIntegerField(default=50)),
                ('pena', models.PositiveIntegerField(default=82)),
                ('active_pena', models.PositiveIntegerField(default=109)),
                ('cashback_percent', models.PositiveIntegerField(default=10)),
                ('cashback_use', models.PositiveIntegerField(default=5000)),
            ],
        ),
        migrations.CreateModel(
            name='TakenMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='box.box')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('box', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='box.box')),
            ],
        ),
        migrations.CreateModel(
            name='CashBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='box.customer')),
            ],
        ),
    ]
