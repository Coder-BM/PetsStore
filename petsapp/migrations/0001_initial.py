# Generated by Django 4.2.1 on 2023-06-01 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('species', models.CharField(max_length=30)),
                ('breed', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('image', models.ImageField(upload_to='media')),
                ('desc', models.TextField(max_length=1000)),
            ],
        ),
    ]