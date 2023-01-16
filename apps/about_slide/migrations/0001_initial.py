# Generated by Django 3.2.7 on 2023-01-03 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='Alex', max_length=15, verbose_name='Name')),
            ],
            options={
                'db_table': 'portfolio',
            },
        ),
    ]
