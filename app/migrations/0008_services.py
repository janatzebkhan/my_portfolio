# Generated by Django 5.0.6 on 2024-06-14 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_professional_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emoji', models.CharField(blank=True, max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
