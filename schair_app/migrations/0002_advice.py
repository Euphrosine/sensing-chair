# Generated by Django 4.2.5 on 2023-10-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schair_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=100, unique=True)),
                ('advice', models.TextField()),
            ],
        ),
    ]
