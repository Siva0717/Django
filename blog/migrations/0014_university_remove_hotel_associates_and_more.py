# Generated by Django 5.0.6 on 2024-09-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_hotel_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='university',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('course', models.IntegerField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='associates',
        ),
        migrations.AlterField(
            model_name='hotel',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]