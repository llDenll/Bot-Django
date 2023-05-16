# Generated by Django 4.1.7 on 2023-03-24 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Імʼя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Прізвище')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Person',
            },
        ),
    ]
