# Generated by Django 5.1.3 on 2024-12-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0003_alter_rsvp_food_alter_rsvp_presence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField(blank=True, null=True)),
                ('string_ids', models.TextField()),
                ('item_titles', models.TextField()),
                ('item_price', models.FloatField()),
            ],
        ),
    ]
