# Generated by Django 5.0.6 on 2024-08-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_hotel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='password',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
