# Generated by Django 3.2.8 on 2023-10-02 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20231002_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.FloatField(blank=True, default=199.99, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='events')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['name'],
            },
        ),
    ]
