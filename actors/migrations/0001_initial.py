# Generated by Django 5.0 on 2023-12-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, choices=[('USA', 'Estados Unidos'), ('BRAZIL', 'Brasil')], max_length=100, null=True)),
            ],
        ),
    ]
