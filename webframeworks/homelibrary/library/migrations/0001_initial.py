# Generated by Django 4.2.5 on 2023-10-04 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('surname', models.CharField(max_length=250)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('genre', models.CharField(max_length=250)),
                ('reading_status', models.CharField(choices=[('TR', 'ToRead'), ('F', 'Finished'), ('R', 'Reading'), ('A', 'Abandoned')], default='TR', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author')),
            ],
        ),
    ]
