# Generated by Django 5.0.6 on 2024-06-14 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='partners_images/')),
                ('category', models.CharField(max_length=50)),
                ('category_1', models.CharField(max_length=50)),
                ('quets', models.TextField()),
            ],
        ),
    ]
