# Generated by Django 5.1.2 on 2024-10-11 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
            ],
        ),
    ]
