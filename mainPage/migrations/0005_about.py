# Generated by Django 5.0.7 on 2024-08-02 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0004_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
