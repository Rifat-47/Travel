# Generated by Django 5.0.2 on 2024-02-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='pics')),
                ('demo', models.CharField(max_length=20)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField()),
            ],
        ),
    ]
