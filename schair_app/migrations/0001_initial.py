# Generated by Django 4.2.5 on 2023-12-11 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchairData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('activity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('schair_data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='schair_app.schairdata')),
                ('advice_text', models.TextField()),
            ],
        ),
    ]
