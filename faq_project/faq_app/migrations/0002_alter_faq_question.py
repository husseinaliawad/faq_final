# Generated by Django 5.1.3 on 2024-11-30 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.TextField(),
        ),
    ]
