# Generated by Django 4.2.4 on 2023-09-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('classfied', models.CharField(blank=True, max_length=200)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
